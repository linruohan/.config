using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using SpeechLib;
using System.IO;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        SpVoice voice = new SpVoice();
        StreamReader sr;
        SpeechLib.SpFileStream sfs=new SpeechLib.SpFileStream();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SpVoice voice = new SpVoice();
            string spf="D:/233.mp3";
            sfs.Open(spf,SpeechLib.SpeechStreamFileMode.SSFMCreateForWrite,false);
            //voice.AudioOutputStream=sfs;
            voice.Rate = 0; //语速,[-10,10]
            voice.Volume = 100; //音量,[0,100]
            voice.Voice = voice.GetVoices().Item(2); //语音库
            voice.Speak("中文speech");
            label1.Text = "Status :  BUSY!";
            while (sr.EndOfStream != true)
            {
                string sl = sr.ReadLine();
                voice.Speak(sl);
            }
            sfs.Close();
            label1.Text = "Status :  Ready.";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog file1=new OpenFileDialog();
            file1.Filter="Text File|*.txt";
            if(file1.ShowDialog()==DialogResult.OK)
            {
                label1.Text = file1.FileName;
                //sr=File.OpenText(file1.FileName);
                sr = new StreamReader(file1.FileName, System.Text.Encoding.Default);    //txt文件默认是ANSI编码，而NT系统默认是Unicode，防止编码错乱导致不认中文
            }
        }
    }
}
