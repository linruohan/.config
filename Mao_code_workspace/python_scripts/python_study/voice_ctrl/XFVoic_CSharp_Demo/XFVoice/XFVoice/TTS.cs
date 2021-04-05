namespace XFVoice
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Runtime.InteropServices;
    using System.Text;

    public class TTS
    {
        private int _bgs = 0;
        private string _ent = "intp65";
        private EnuSpeeker _enumSpeeker;
        private string _errorMsg;
        private int _rdn = 3;
        private string _spd = "default";
        private Dictionary<EnuSpeeker, string> _speekerDic;
        private string _vcn = "xiaoyan";
        private string _vol = "default";
        private string beginParam = "ssm=1,auf=audio/L16;rate=16000,rdn=1,vcn=xiaoyan,ent=intp65,vol=default";
        private string configs = "server_url=dev.voicecloud.cn:1028/index.htm,timeout=10000,coding_libs=speex.dll,appid=52a296c2,max_text_size=4096";

        public TTS()
        {
            this._speekerDic = new Dictionary<EnuSpeeker, string>();
            this._speekerDic.Add(EnuSpeeker.小燕_青年女声_中英文_普通话, "ent=intp65,vcn=xiaoyan");
            this._speekerDic.Add(EnuSpeeker.小宇_青年男声_中英文_普通话, "ent=intp65,vcn=xiaoyu");
            this._speekerDic.Add(EnuSpeeker.小研_青年女声_中英文_普通话, "ent=vivi21,vcn=vixy");
            this._speekerDic.Add(EnuSpeeker.小琪_青年女声_中英文_普通话, "ent=vivi21,vcn=vixq");
            this._speekerDic.Add(EnuSpeeker.小峰_青年男声_中英文_普通话, "ent=vivi21,vcn=vixf");
            this._speekerDic.Add(EnuSpeeker.小梅_青年女声_中英文_粤语, "ent=vivi21,vcn=vixm");
            this._speekerDic.Add(EnuSpeeker.小莉_青年女声_中英文_台普, "ent=vivi21,vcn=vixl");
            this._speekerDic.Add(EnuSpeeker.小蓉_青年女声_汉语_四川话, "ent=vivi21,vcn=vixr");
            this._speekerDic.Add(EnuSpeeker.小芸_青年女声_汉语_东北话, "ent=vivi21,vcn=vixyun");
            this._speekerDic.Add(EnuSpeeker.小坤_青年男声_汉语_河南话, "ent=vivi21,vcn=vixk");
            this._speekerDic.Add(EnuSpeeker.小强_青年男声_汉语_湖南话, "ent=vivi21,vcn=vixqa");
            this._speekerDic.Add(EnuSpeeker.小莹_青年女声_汉语_陕西话, "ent=vivi21,vcn=vixying");
            this._speekerDic.Add(EnuSpeeker.老孙_老年男声_汉语_普通话, "ent=vivi21,vcn=vils");
        }

        private string GetSpeeker()
        {
            string str = "";
            try
            {
                if (!string.IsNullOrEmpty(this._enumSpeeker.ToString()))
                {
                    return this._speekerDic[this._enumSpeeker];
                }
                str = "vcn=xiaoyan,ent=intp65";
            }
            catch
            {
            }
            return str;
        }

        private WAVE_Header getWave_Header(int data_len)
        {
            return new WAVE_Header { RIFF_ID = 0x46464952, File_Size = data_len + 0x24, RIFF_Type = 0x45564157, FMT_ID = 0x20746d66, FMT_Size = 0x10, FMT_Tag = 1, FMT_Channel = 1, FMT_SamplesPerSec = 0x3e80, AvgBytesPerSec = 0x7d00, BlockAlign = 2, BitsPerSample = 0x10, DATA_ID = 0x61746164, DATA_Size = data_len };
        }

        private byte[] StructToBytes(object structure)
        {
            byte[] buffer;
            int cb = Marshal.SizeOf(structure);
            IntPtr ptr = Marshal.AllocHGlobal(cb);
            try
            {
                Marshal.StructureToPtr(structure, ptr, false);
                byte[] destination = new byte[cb];
                Marshal.Copy(ptr, destination, 0, cb);
                buffer = destination;
            }
            finally
            {
                Marshal.FreeHGlobal(ptr);
            }
            return buffer;
        }

        public bool TextToSpeek(string txt, string outWaveFlie)
        {
            if (string.IsNullOrEmpty(txt) || string.IsNullOrEmpty(outWaveFlie))
            {
                this._errorMsg = "无文本或文件路径为空";
                return false;
            }
            MemoryStream stream = null;
            FileStream stream2 = null;
            try
            {
                string str = "";
                int num = -1;
                int errorCode = -1;
                int num3 = -1;
                int num5 = -1;
                num = MscDll.QTTSInit(this.configs);
                if (num != 0)
                {
                    this._errorMsg = "初始化失败,错误码：" + num;
                    return false;
                }
                this.beginParam = string.Format("ssm=1,auf=audio/L16;rate=16000,{0},vol={1},spd={2},rdn={2},bgs={4}", new object[] { this.GetSpeeker(), this._vol, this._spd, this._rdn, this._bgs });
                str = Marshal.PtrToStringAnsi(MscDll.QTTSSessionBegin(this.beginParam, ref errorCode));
                if (string.IsNullOrEmpty(str))
                {
                    this._errorMsg = "开始合成失败,错误码：" + errorCode;
                    return false;
                }
                num5 = MscDll.QTTSTextPut(str, txt, (uint) Encoding.Default.GetBytes(txt).Length, "");
                if (num5 != 0)
                {
                    this._errorMsg = "合成请求失败,错误码：" + num5;
                    return false;
                }
                int audioLen = 0;
                int synthStatus = 1;
                int num8 = -1;
                stream = new MemoryStream();
                stream.Write(new byte[0x2c], 0, 0x2c);
                while (synthStatus == 1)
                {
                    IntPtr source = MscDll.QTTSAudioGet(str, ref audioLen, ref synthStatus, ref num8);
                    if (num8 != 0)
                    {
                        this._errorMsg = "获取合成后的数据失败,错误码：" + num5;
                        return false;
                    }
                    byte[] destination = new byte[audioLen];
                    if (audioLen > 0)
                    {
                        Marshal.Copy(source, destination, 0, audioLen);
                    }
                    stream.Write(destination, 0, audioLen);
                }
                WAVE_Header structure = this.getWave_Header(((int) stream.Length) - 0x2c);
                byte[] buffer2 = this.StructToBytes(structure);
                stream.Position = 0L;
                stream.Write(buffer2, 0, buffer2.Length);
                stream.Position = 0L;
                stream2 = new FileStream(outWaveFlie, FileMode.Create);
                stream.WriteTo(stream2);
                stream2.Close();
                stream.Close();
                num3 = MscDll.QTTSSessionEnd(str, "normal end");
                int num9 = MscDll.QTTSFini();
                return true;
            }
            catch (Exception exception)
            {
                this._errorMsg = "TTS合成异常:" + exception.Message;
            }
            finally
            {
                if (stream2 != null)
                {
                    stream2.Close();
                }
                if (stream != null)
                {
                    stream.Close();
                }
                MscDll.QTTSFini();
            }
            return false;
        }

        public int Bgs
        {
            get
            {
                return this._bgs;
            }
            set
            {
                this._bgs = value;
            }
        }

        public EnuSpeeker EnumSpeeker
        {
            get
            {
                return this._enumSpeeker;
            }
            set
            {
                this._enumSpeeker = value;
            }
        }

        public string ErrorMsg
        {
            get
            {
                return this._errorMsg;
            }
            set
            {
                this._errorMsg = value;
            }
        }

        public int Rdn
        {
            get
            {
                return this._rdn;
            }
            set
            {
                this._rdn = value;
            }
        }

        public string Spd
        {
            get
            {
                return this._spd;
            }
            set
            {
                if (!string.IsNullOrEmpty(value))
                {
                    this._spd = value;
                }
            }
        }

        private Dictionary<EnuSpeeker, string> SpeekerDic
        {
            get
            {
                return this._speekerDic;
            }
            set
            {
                this._speekerDic = value;
            }
        }

        public string Vol
        {
            get
            {
                return this._vol;
            }
            set
            {
                if (!string.IsNullOrEmpty(value))
                {
                    this._vol = value;
                }
            }
        }
    }
}

