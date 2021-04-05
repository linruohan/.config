using System;
using System.Collections.Generic;
using System.Text;

namespace XFVoice
{
    class Program
    {
        static void Main()
        {
            XFVoice.TTS tts = new TTS();

            string outputFile = "D:/test.wav";
            string txtStr = "尊敬的王淑一女士，您好，您本月尚欠费20元,请于8月20日前缴清欠费，谢谢。";

            tts.TextToSpeek(txtStr, outputFile);

            if (System.IO.File.Exists(outputFile))
            {
                Console.WriteLine("合成成功");
            }
 

            Console.ReadKey();
        }

    }
}
