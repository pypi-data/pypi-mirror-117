"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Stream = void 0;
const fs_1 = require("fs");
const events_1 = require("events");
const wrtc_1 = require("wrtc");
const binding_1 = require("./binding");
class Stream extends events_1.EventEmitter {
    constructor(filePath, bitsPerSample = 16, sampleRate = 48000, channelCount = 1, buffer_length = 10, timePulseBuffer = buffer_length == 4 ? 1.5 : 0) {
        super();
        this.filePath = filePath;
        this.bitsPerSample = bitsPerSample;
        this.sampleRate = sampleRate;
        this.channelCount = channelCount;
        this.buffer_length = buffer_length;
        this.timePulseBuffer = timePulseBuffer;
        this.paused = false;
        this.finished = true;
        this.stopped = false;
        this.finishedLoading = false;
        this.bytesLoaded = 0;
        this.bytesSpeed = 0;
        this.lastLag = 0;
        this.equalCount = 0;
        this.lastBytesLoaded = 0;
        this.finishedBytes = false;
        this.lastByteCheck = 0;
        this.lastByte = 0;
        this.runningPulse = false;
        this.endListener = (() => {
            this.finishedLoading = true;
            binding_1.Binding.log('COMPLETED_BUFFERING -> ' + new Date().getTime(), binding_1.Binding.DEBUG);
            binding_1.Binding.log('BYTES_STREAM_CACHE_LENGTH -> ' + this.cache.length, binding_1.Binding.DEBUG);
            binding_1.Binding.log('BYTES_LOADED -> ' +
                this.bytesLoaded +
                'OF -> ' +
                Stream.getFilesizeInBytes(this.filePath), binding_1.Binding.DEBUG);
        }).bind(this);
        this.dataListener = ((data) => {
            this.bytesLoaded += data.length;
            this.bytesSpeed = data.length;
            try {
                if (!this.needsBuffering()) {
                    this.readable?.pause();
                    this.runningPulse = false;
                    binding_1.Binding.log('ENDED_BUFFERING -> ' + new Date().getTime(), binding_1.Binding.DEBUG);
                    binding_1.Binding.log('BYTES_STREAM_CACHE_LENGTH -> ' + this.cache.length, binding_1.Binding.DEBUG);
                    binding_1.Binding.log('PULSE -> ' + this.runningPulse, binding_1.Binding.DEBUG);
                }
            }
            catch (e) {
                this.emit('stream_deleted');
                return;
            }
            binding_1.Binding.log('BYTES_LOADED -> ' +
                this.bytesLoaded +
                'OF -> ' +
                Stream.getFilesizeInBytes(this.filePath), binding_1.Binding.DEBUG);
            this.cache = Buffer.concat([this.cache, data]);
        }).bind(this);
        this.audioSource = new wrtc_1.nonstandard.RTCAudioSource();
        this.cache = Buffer.alloc(0);
        this.paused = true;
        this.setReadable(this.filePath);
        this.processData();
    }
    setReadable(filePath) {
        this.bytesLoaded = 0;
        this.bytesSpeed = 0;
        this.lastLag = 0;
        this.equalCount = 0;
        this.lastBytesLoaded = 0;
        this.finishedBytes = false;
        this.lastByteCheck = 0;
        this.lastByte = 0;
        if (this.readable) {
            this.readable.removeListener('data', this.dataListener);
            this.readable.removeListener('end', this.endListener);
        }
        this.filePath = filePath;
        this.readable = fs_1.createReadStream(filePath);
        if (this.stopped) {
            throw new Error('Cannot set readable when stopped');
        }
        this.cache = Buffer.alloc(0);
        if (this.readable !== undefined) {
            this.finished = false;
            this.finishedLoading = false;
            this.readable.on('data', this.dataListener);
            this.readable.on('end', this.endListener);
        }
    }
    static getFilesizeInBytes(path) {
        return fs_1.statSync(path).size;
    }
    needsBuffering(withPulseCheck = true) {
        if (this.finishedLoading) {
            return false;
        }
        const byteLength = ((this.sampleRate * this.bitsPerSample) / 8 / 100) *
            this.channelCount;
        let result = this.cache.length < byteLength * 100 * this.buffer_length;
        result =
            result &&
                (this.bytesLoaded <
                    Stream.getFilesizeInBytes(this.filePath) -
                        this.bytesSpeed * 2 ||
                    this.finishedBytes);
        if (this.timePulseBuffer > 0 && withPulseCheck) {
            result = result && this.runningPulse;
        }
        return result;
    }
    checkLag() {
        if (this.finishedLoading) {
            return false;
        }
        const byteLength = ((this.sampleRate * this.bitsPerSample) / 8 / 100) *
            this.channelCount;
        return this.cache.length < byteLength * 100;
    }
    pause() {
        if (this.stopped) {
            throw new Error('Cannot pause when stopped');
        }
        this.paused = true;
        this.emit('pause', this.paused);
    }
    resume() {
        if (this.stopped) {
            throw new Error('Cannot resume when stopped');
        }
        this.paused = false;
        this.emit('resume', this.paused);
    }
    finish() {
        this.finished = true;
    }
    stop() {
        this.finish();
        this.stopped = true;
    }
    createTrack() {
        return this.audioSource.createTrack();
    }
    getIdSource() {
        return this.audioSource;
    }
    processData() {
        const oldTime = new Date().getTime();
        if (this.stopped) {
            return;
        }
        const byteLength = ((this.sampleRate * this.bitsPerSample) / 8 / 100) *
            this.channelCount;
        if (!(!this.finished &&
            this.finishedLoading &&
            this.cache.length < byteLength)) {
            try {
                if (this.needsBuffering(false)) {
                    let checkBuff = true;
                    if (this.timePulseBuffer > 0) {
                        this.runningPulse =
                            this.cache.length <
                                byteLength * 100 * this.timePulseBuffer;
                        checkBuff = this.runningPulse;
                    }
                    if (this.readable !== undefined && checkBuff) {
                        binding_1.Binding.log('PULSE -> ' + this.runningPulse, binding_1.Binding.DEBUG);
                        this.readable.resume();
                        binding_1.Binding.log('BUFFERING -> ' + new Date().getTime(), binding_1.Binding.DEBUG);
                    }
                }
            }
            catch (e) {
                this.emit('stream_deleted');
                return;
            }
            const checkLag = this.checkLag();
            let fileSize;
            try {
                if (oldTime - this.lastByteCheck > 1000) {
                    fileSize = Stream.getFilesizeInBytes(this.filePath);
                    this.lastByte = fileSize;
                    this.lastByteCheck = oldTime;
                }
                else {
                    fileSize = this.lastByte;
                }
            }
            catch (e) {
                this.emit('stream_deleted');
                return;
            }
            if (!this.paused &&
                !this.finished &&
                (this.cache.length >= byteLength || this.finishedLoading) &&
                !checkLag) {
                const buffer = this.cache.slice(0, byteLength);
                const samples = new Int16Array(new Uint8Array(buffer).buffer);
                this.cache = this.cache.slice(byteLength);
                try {
                    this.audioSource.onData({
                        bitsPerSample: this.bitsPerSample,
                        sampleRate: this.sampleRate,
                        channelCount: this.channelCount,
                        numberOfFrames: samples.length,
                        samples,
                    });
                }
                catch (error) {
                    this.emit('error', error);
                }
            }
            else if (checkLag) {
                binding_1.Binding.log('STREAM_LAG -> ' + new Date().getTime(), binding_1.Binding.DEBUG);
                binding_1.Binding.log('BYTES_STREAM_CACHE_LENGTH -> ' + this.cache.length, binding_1.Binding.DEBUG);
                binding_1.Binding.log('BYTES_LOADED -> ' +
                    this.bytesLoaded +
                    'OF -> ' +
                    Stream.getFilesizeInBytes(this.filePath), binding_1.Binding.DEBUG);
            }
            if (!this.finishedLoading) {
                if (fileSize === this.lastBytesLoaded) {
                    if (this.equalCount >= 15) {
                        this.equalCount = 0;
                        binding_1.Binding.log('NOT_ENOUGH_BYTES -> ' + oldTime, binding_1.Binding.DEBUG);
                        this.finishedBytes = true;
                        this.readable?.resume();
                    }
                    else {
                        if (oldTime - this.lastLag > 1000) {
                            this.equalCount += 1;
                            this.lastLag = oldTime;
                        }
                    }
                }
                else {
                    this.lastBytesLoaded = fileSize;
                    this.equalCount = 0;
                    this.finishedBytes = false;
                }
            }
        }
        if (!this.finished &&
            this.finishedLoading &&
            this.cache.length < byteLength) {
            this.finish();
            this.emit('finish');
        }
        const toSubtract = new Date().getTime() - oldTime;
        setTimeout(() => this.processData(), (this.finished || this.paused || this.checkLag() ? 500 : 10) -
            toSubtract);
    }
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}
exports.Stream = Stream;
