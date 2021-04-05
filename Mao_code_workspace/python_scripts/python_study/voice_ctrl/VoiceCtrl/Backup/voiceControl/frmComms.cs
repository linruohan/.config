using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Xml;

namespace voiceControl
{
    public partial class frmComms : Form
    {
        public frmComms()
        {
            InitializeComponent();
        }

        private void frmComms_Load(object sender, EventArgs e)
        {
            lstComms.Items.Clear();
            XmlDocument xdoc = new XmlDocument();
            xdoc.Load(Application.StartupPath + @"\rules.xml");
            getNode((XmlNode)xdoc.DocumentElement);

        }

        private void getNode(XmlNode root)
        {
            if (root == null) return;
            if (root is XmlElement)
            {
                if (root.Name == "P")
                    lstComms.Items.Add(root.InnerText);
                if (root.HasChildNodes)
                    getNode(root.FirstChild);
                if (root.NextSibling != null)
                    getNode(root.NextSibling);
            }
        }

        private void btClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}