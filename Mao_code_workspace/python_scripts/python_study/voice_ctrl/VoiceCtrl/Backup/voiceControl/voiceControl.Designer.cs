namespace voiceControl
{
    partial class voiceCtr
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(voiceCtr));
            this.lstCommand = new System.Windows.Forms.ListBox();
            this.btnControl = new System.Windows.Forms.Button();
            this.btnClose = new System.Windows.Forms.Button();
            this.conMenu = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.miStart = new System.Windows.Forms.ToolStripMenuItem();
            this.miStop = new System.Windows.Forms.ToolStripMenuItem();
            this.miDisp = new System.Windows.Forms.ToolStripMenuItem();
            this.miClose = new System.Windows.Forms.ToolStripMenuItem();
            this.status = new System.Windows.Forms.StatusStrip();
            this.staLab1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.staLab2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.notify = new System.Windows.Forms.NotifyIcon(this.components);
            this.btnStopCtr = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.miComm = new System.Windows.Forms.ToolStripMenuItem();
            this.conMenu.SuspendLayout();
            this.status.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // lstCommand
            // 
            this.lstCommand.FormattingEnabled = true;
            this.lstCommand.ItemHeight = 12;
            this.lstCommand.Location = new System.Drawing.Point(1, 1);
            this.lstCommand.Name = "lstCommand";
            this.lstCommand.Size = new System.Drawing.Size(131, 196);
            this.lstCommand.TabIndex = 0;
            // 
            // btnControl
            // 
            this.btnControl.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnControl.Location = new System.Drawing.Point(151, 112);
            this.btnControl.Name = "btnControl";
            this.btnControl.Size = new System.Drawing.Size(65, 23);
            this.btnControl.TabIndex = 1;
            this.btnControl.Text = "开始控制";
            this.btnControl.UseVisualStyleBackColor = true;
            this.btnControl.Click += new System.EventHandler(this.btnControl_Click);
            // 
            // btnClose
            // 
            this.btnClose.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnClose.Location = new System.Drawing.Point(151, 170);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(65, 23);
            this.btnClose.TabIndex = 2;
            this.btnClose.Text = "关闭程序";
            this.btnClose.UseVisualStyleBackColor = true;
            this.btnClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // conMenu
            // 
            this.conMenu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.miStart,
            this.miStop,
            this.miDisp,
            this.miComm,
            this.miClose});
            this.conMenu.Name = "conMenu";
            this.conMenu.Size = new System.Drawing.Size(153, 136);
            // 
            // miStart
            // 
            this.miStart.Name = "miStart";
            this.miStart.Size = new System.Drawing.Size(152, 22);
            this.miStart.Text = "开始控制";
            this.miStart.Click += new System.EventHandler(this.btnControl_Click);
            // 
            // miStop
            // 
            this.miStop.Name = "miStop";
            this.miStop.Size = new System.Drawing.Size(152, 22);
            this.miStop.Text = "停止控制";
            this.miStop.Click += new System.EventHandler(this.btnStopCtr_Click);
            // 
            // miDisp
            // 
            this.miDisp.Name = "miDisp";
            this.miDisp.Size = new System.Drawing.Size(152, 22);
            this.miDisp.Text = "显示界面";
            this.miDisp.Click += new System.EventHandler(this.miDisp_Click);
            // 
            // miClose
            // 
            this.miClose.Name = "miClose";
            this.miClose.Size = new System.Drawing.Size(152, 22);
            this.miClose.Text = "关闭程序";
            this.miClose.Click += new System.EventHandler(this.btnClose_Click);
            // 
            // status
            // 
            this.status.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.staLab1,
            this.staLab2,
            this.toolStripStatusLabel1});
            this.status.Location = new System.Drawing.Point(0, 198);
            this.status.Name = "status";
            this.status.Size = new System.Drawing.Size(224, 22);
            this.status.TabIndex = 4;
            this.status.Text = "statusStrip1";
            // 
            // staLab1
            // 
            this.staLab1.AutoSize = false;
            this.staLab1.BorderSides = System.Windows.Forms.ToolStripStatusLabelBorderSides.Right;
            this.staLab1.Name = "staLab1";
            this.staLab1.Size = new System.Drawing.Size(100, 17);
            this.staLab1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // staLab2
            // 
            this.staLab2.Name = "staLab2";
            this.staLab2.Size = new System.Drawing.Size(0, 17);
            this.staLab2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(131, 12);
            this.toolStripStatusLabel1.Text = "toolStripStatusLabel1";
            // 
            // notify
            // 
            this.notify.BalloonTipIcon = System.Windows.Forms.ToolTipIcon.Info;
            this.notify.BalloonTipText = "右击此处可设置语音控制属性";
            this.notify.BalloonTipTitle = "语音控制";
            this.notify.ContextMenuStrip = this.conMenu;
            this.notify.Icon = ((System.Drawing.Icon)(resources.GetObject("notify.Icon")));
            this.notify.Text = "语音控制";
            this.notify.Visible = true;
            this.notify.MouseDown += new System.Windows.Forms.MouseEventHandler(this.notify_MouseDown);
            // 
            // btnStopCtr
            // 
            this.btnStopCtr.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.btnStopCtr.Location = new System.Drawing.Point(151, 141);
            this.btnStopCtr.Name = "btnStopCtr";
            this.btnStopCtr.Size = new System.Drawing.Size(65, 23);
            this.btnStopCtr.TabIndex = 6;
            this.btnStopCtr.Text = "停止控制";
            this.btnStopCtr.UseVisualStyleBackColor = true;
            this.btnStopCtr.Click += new System.EventHandler(this.btnStopCtr_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(144, 1);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(72, 100);
            this.pictureBox1.TabIndex = 12;
            this.pictureBox1.TabStop = false;
            // 
            // miComm
            // 
            this.miComm.Name = "miComm";
            this.miComm.Size = new System.Drawing.Size(152, 22);
            this.miComm.Text = "命令列表";
            this.miComm.Click += new System.EventHandler(this.miComm_Click);
            // 
            // voiceCtr
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(224, 220);
            this.Controls.Add(this.status);
            this.Controls.Add(this.lstCommand);
            this.Controls.Add(this.btnControl);
            this.Controls.Add(this.btnStopCtr);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.btnClose);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "voiceCtr";
            this.ShowInTaskbar = false;
            this.Text = "语音控制";
            this.Resize += new System.EventHandler(this.voiceCtr_Resize);
            this.Load += new System.EventHandler(this.voiceCtr_Load);
            this.conMenu.ResumeLayout(false);
            this.status.ResumeLayout(false);
            this.status.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox lstCommand;
        private System.Windows.Forms.Button btnControl;
        private System.Windows.Forms.Button btnClose;
        private System.Windows.Forms.ContextMenuStrip conMenu;
        private System.Windows.Forms.StatusStrip status;
        private System.Windows.Forms.ToolStripStatusLabel staLab1;
        private System.Windows.Forms.ToolStripStatusLabel staLab2;
        private System.Windows.Forms.NotifyIcon notify;
        private System.Windows.Forms.ToolStripMenuItem miStart;
        private System.Windows.Forms.ToolStripMenuItem miStop;
        private System.Windows.Forms.ToolStripMenuItem miClose;
        private System.Windows.Forms.Button btnStopCtr;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.ToolStripMenuItem miDisp;
        private System.Windows.Forms.ToolStripMenuItem miComm;
    }
}

