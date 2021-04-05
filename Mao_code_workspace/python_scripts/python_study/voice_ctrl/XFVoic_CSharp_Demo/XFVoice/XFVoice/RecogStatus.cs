namespace XFVoice
{
    using System;

    public enum RecogStatus
    {
        ISR_REC_NULL = -1,
        ISR_REC_STATUS_INCOMPLETE = 2,
        ISR_REC_STATUS_MAX_CPU_TIME = 6,
        ISR_REC_STATUS_MAX_SPEECH = 7,
        ISR_REC_STATUS_NO_MATCH = 1,
        ISR_REC_STATUS_NO_SPEECH_FOUND = 10,
        ISR_REC_STATUS_NON_SPEECH_DETECTED = 3,
        ISR_REC_STATUS_REJECTED = 9,
        ISR_REC_STATUS_SPEECH_COMPLETE = 5,
        ISR_REC_STATUS_SPEECH_DETECTED = 4,
        ISR_REC_STATUS_STOPPED = 8,
        ISR_REC_STATUS_SUCCESS = 0
    }
}

