"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.RTCConnection = void 0;
const tgcalls_1 = require("./tgcalls");
const binding_1 = require("./binding");
class RTCConnection {
    constructor(chatId, filePath, binding, bitrate, bufferLength, inviteHash) {
        this.chatId = chatId;
        this.filePath = filePath;
        this.binding = binding;
        this.bitrate = bitrate;
        this.bufferLength = bufferLength;
        this.inviteHash = inviteHash;
        this.tgcalls = new tgcalls_1.TGCalls({ chatId: this.chatId });
        this.stream = new tgcalls_1.Stream(filePath, 16, bitrate, 1, bufferLength);
        this.tgcalls.joinVoiceCall = async (payload) => {
            payload = {
                chat_id: this.chatId,
                ufrag: payload.ufrag,
                pwd: payload.pwd,
                hash: payload.hash,
                setup: payload.setup,
                fingerprint: payload.fingerprint,
                source: payload.source,
                invite_hash: this.inviteHash,
            };
            binding_1.Binding.log('callJoinPayload -> ' + JSON.stringify(payload), binding_1.Binding.INFO);
            const joinCallResult = await this.binding.sendUpdate({
                action: 'join_voice_call_request',
                payload: payload,
            });
            binding_1.Binding.log('joinCallRequestResult -> ' + JSON.stringify(joinCallResult), binding_1.Binding.INFO);
            return joinCallResult;
        };
        this.stream.on('finish', async () => {
            await this.binding.sendUpdate({
                action: 'stream_ended',
                chat_id: chatId,
            });
        });
        this.stream.on('stream_deleted', async () => {
            this.stream.stop();
            await this.binding.sendUpdate({
                action: 'update_request',
                result: 'STREAM_DELETED',
                chat_id: chatId,
            });
        });
    }
    async joinCall() {
        try {
            let result = await this.tgcalls.start(this.stream.createTrack());
            this.stream.resume();
            return result;
        }
        catch (e) {
            this.stream.stop();
            binding_1.Binding.log('joinCallError -> ' + e.toString(), binding_1.Binding.INFO);
            return false;
        }
    }
    stop() {
        try {
            this.stream.stop();
            this.tgcalls.close();
        }
        catch (e) { }
    }
    async leave_call() {
        try {
            this.stop();
            return await this.binding.sendUpdate({
                action: 'leave_call_request',
                chat_id: this.chatId,
            });
        }
        catch (e) {
            return {
                action: 'REQUEST_ERROR',
                message: e.toString(),
            };
        }
    }
    pause() {
        this.stream.pause();
    }
    async resume() {
        this.stream.resume();
    }
    changeStream(filePath) {
        this.filePath = filePath;
        this.stream.setReadable(this.filePath);
    }
}
exports.RTCConnection = RTCConnection;
