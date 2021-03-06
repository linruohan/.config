using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows;
using System.Windows.Forms;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Xml;
using SpeechLib;

namespace voiceControl
{
    public partial class voiceCtr : Form
    {
        enum MouseEventFlag : uint
        {
            Move = 0x0001,
            LeftDown = 0x0002,
            LeftUp = 0x0004,
            RightDown = 0x0008,
            RightUp = 0x0010,
            MiddleDown = 0x0020,
            MiddleUp = 0x0040,
            XDown = 0x0080,
            XUp = 0x0100,
            Wheel = 0x0800,
            VirtualDesk = 0x4000,
            Absolute = 0x8000
        }
        const int WM_CLOSE = 0x0010;
       
        [DllImport("user32.dll", EntryPoint = "GetForegroundWindow")]
        private static extern IntPtr GetForegroundWindow();

        [DllImport("user32.dll", EntryPoint = "PostMessage")]
        static extern int PostMessage(IntPtr hWnd, int Msg, int wParam, int lParam);       

        [DllImport("user32.dll")]
        static extern void mouse_event(MouseEventFlag flags, int dx, int dy, uint data, IntPtr extraInfo);
        
        
        public SpSharedRecoContext ssrc;
        public ISpeechRecoGrammar isrgComm;
        public Boolean blMove = false;
        
        public voiceCtr()
        {
            InitializeComponent();
        }

        private void voiceCtr_Load(object sender, EventArgs e)
        {   
            try
            {
                ssrc = new SpSharedRecoContext();                
                isrgComm = ssrc.CreateGrammar(0);
                string fileName = Application.StartupPath + @"\rules.xml";
                isrgComm.CmdLoadFromFile(fileName, SpeechLoadOption.SLODynamic);
                _ISpeechRecoContextEvents_RecognitionEventHandler recHandle = new _ISpeechRecoContextEvents_RecognitionEventHandler(Recognition);
                ssrc.Recognition += recHandle;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            this.WindowState = FormWindowState.Minimized;
            Command();
        }

        //Command&Control
        private void Command()
        {
            ssrc.Pause();
            isrgComm.State = SpeechGrammarState.SGSEnabled;
            staLab1.Text = "���ڿ��ơ���";
            notify.Icon = new Icon("vCtrl.ico");
            isrgComm.CmdSetRuleIdState(0, SpeechRuleState.SGDSActive);
            ssrc.Resume();
        }

        //Stop Control
        private void stopControl()
        {            
            ssrc.Pause();            
            isrgComm.State = SpeechGrammarState.SGSDisabled;            
            notify.Icon = new Icon("vCtrlStop.ico");
            ssrc.Resume();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnControl_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
            notify.Visible = true;
            Command();
        }

        private void Recognition(int iIndex, Object obj, SpeechRecognitionType CognitionType, ISpeechRecoResult result)
        {
            string sRe = result.PhraseInfo.GetText(0, -1, true);
            staLab2.Text = sRe;
            sRe = sRe.Trim();
            IntPtr hwnd;
            //�����ʶ����            
            lstCommand.Items.Add(sRe);
            staLab1.Text = "���ڿ��ơ���";
            switch (sRe)
            {                
                case "ֹͣ����":
                    stopControl();
                    break;                
                case "������":
                    SendKeys.Send("{PGDN}");
                    break;
                case "��":
                    SendKeys.Send("{PGDN}");
                    break;
                case "��ҳ":
                    SendKeys.Send("{PGDN}");
                    break;
                case "�·�":
                    SendKeys.Send("{PGDN}");
                    break;
                case "���氢��":
                    SendKeys.Send("{PGUP}");
                    break;
                case "�Ϸ�":
                    SendKeys.Send("{PGUP}");
                    break;                
                case "������":
                    SendKeys.Send("{LEFT}");
                    break;
                case "������":
                    SendKeys.Send("{RIGHT}");
                    break;
                case "����":
                    //staLab2.Text = "�������";
                    Point pt = Cursor.Position;                    
                    mouse_event(MouseEventFlag.LeftDown, pt.X, pt.Y, 0, IntPtr.Zero);
                    mouse_event(MouseEventFlag.LeftUp, pt.X, pt.Y, 0, IntPtr.Zero);
                    break;
                case "�ش���":
                    if (MessageBox.Show("Ҫ�رյ�ǰ���ڣ�", "��������", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                    {
                        hwnd = GetForegroundWindow();
                        staLab1.Text = "�رյ�ǰ����";
                        int iRet = PostMessage(hwnd, WM_CLOSE, 0, 0);
                    }
                    break;
                case "�رճ���":
                    if (MessageBox.Show("Ҫ�ر��������Ƴ�����", "��������", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                    {
                        Application.Exit();
                    }                        
                    break;
            }
        } 

        private void btnStopCtr_Click(object sender, EventArgs e)
        {
            stopControl();
        }

        private void notify_MouseDown(object sender, MouseEventArgs e)
        {
            Point pt = Cursor.Position;
            if (e.Button == MouseButtons.Left)
            {                
                mouse_event(MouseEventFlag.RightUp, pt.X, pt.Y, 0, IntPtr.Zero);
            }
            else
            {
                notify.ContextMenuStrip = conMenu;
            }
        }

        private void miDisp_Click(object sender, EventArgs e)
        {
            this.Visible = true;
            this.WindowState = FormWindowState.Normal;
            notify.Visible = false;            
        }

        private void voiceCtr_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {      
                this.Hide();
                notify.Visible = true;
            }
            else
            {
                this.Show();
                notify.Visible = false;
            }

        }

        private void miComm_Click(object sender, EventArgs e)
        {
            frmComms frmCom = new frmComms();
            frmCom.Show();
        }
        
        
    }
}