namespace voiceControl
{
    partial class frmComms
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmComms));
            this.lstComms = new System.Windows.Forms.ListBox();
            this.btClose = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lstComms
            // 
            this.lstComms.Dock = System.Windows.Forms.DockStyle.Top;
            this.lstComms.FormattingEnabled = true;
            this.lstComms.ItemHeight = 12;
            this.lstComms.Location = new System.Drawing.Point(0, 0);
            this.lstComms.Name = "lstComms";
            this.lstComms.Size = new System.Drawing.Size(187, 232);
            this.lstComms.TabIndex = 1;
            // 
            // btClose
            // 
            this.btClose.Location = new System.Drawing.Point(106, 238);
            this.btClose.Name = "btClose";
            this.btClose.Size = new System.Drawing.Size(75, 23);
            this.btClose.TabIndex = 2;
            this.btClose.Text = "关 闭";
            this.btClose.UseVisualStyleBackColor = true;
            this.btClose.Click += new System.EventHandler(this.btClose_Click);
            // 
            // frmComms
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(187, 266);
            this.Controls.Add(this.btClose);
            this.Controls.Add(this.lstComms);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "frmComms";
            this.Text = "查看命令列表";
            this.Load += new System.EventHandler(this.frmComms_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lstComms;
        private System.Windows.Forms.Button btClose;
    }
}