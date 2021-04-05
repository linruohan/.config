namespace XFVoice
{
    using System;

    public enum AudioStatus
    {
        ISR_AUDIO_SAMPLE_CONTINUE = 2,
        ISR_AUDIO_SAMPLE_END_CHUNK = 0x40,
        ISR_AUDIO_SAMPLE_FIRST = 1,
        ISR_AUDIO_SAMPLE_INIT = 0,
        ISR_AUDIO_SAMPLE_LAST = 4,
        ISR_AUDIO_SAMPLE_LOST = 0x10,
        ISR_AUDIO_SAMPLE_NEW_CHUNK = 0x20,
        ISR_AUDIO_SAMPLE_SUPPRESSED = 8,
        ISR_AUDIO_SAMPLE_VALIDBITS = 0x7f
    }
}

