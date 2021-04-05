namespace XFVoice
{
    using System;
    using System.Runtime.InteropServices;

    public class MscDll
    {
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRAudioWrite(string sessionID, byte[] waveData, uint waveLen, AudioStatus audioStatus, ref EpStatus epStatus, ref RecogStatus recogStatus);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRFini();
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRGetParam(string sessionID, string paramName, string paramValue, ref uint valueLen);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern IntPtr QISRGetResult(string sessionID, ref RecogStatus rsltStatus, int waitTime, ref int errorCode);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRGrammarActivate(string sessionID, string grammar, string type, int weight);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRInit(string configs);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern IntPtr QISRSessionBegin(string grammarList, string _params, ref int errorCode);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern int QISRSessionEnd(string sessionID, string hints);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall)]
        public static extern IntPtr QISRUploadData(string sessionID, string dataName, byte[] userData, uint lenght, string paramValue, ref int errorCode);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern IntPtr QTTSAudioGet(string sessionID, ref int audioLen, ref int synthStatus, ref int errorCode);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern string QTTSAudioInfo(string sessionID);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern int QTTSFini();
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern int QTTSGetParam(string sessionID, string paramName, ref string paramValue, ref int valueLen);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern int QTTSInit(string configs);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern IntPtr QTTSSessionBegin(string _params, ref int errorCode);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern int QTTSSessionEnd(string sessionID, string hints);
        [DllImport("msc.dll", CallingConvention=CallingConvention.StdCall, SetLastError=true)]
        public static extern int QTTSTextPut(string sessionID, string textString, uint textLen, string _params);
    }
}

