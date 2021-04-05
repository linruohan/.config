namespace XFVoice
{
    using System;

    public enum EpStatus
    {
        ISR_EP_AFTER_SPEECH = 3,
        ISR_EP_ERROR = 5,
        ISR_EP_IN_SPEECH = 1,
        ISR_EP_LOOKING_FOR_SPEECH = 0,
        ISR_EP_MAX_SPEECH = 6,
        ISR_EP_NULL = -1,
        ISR_EP_TIMEOUT = 4
    }
}

