using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Windows.Interop;

namespace Example
{
    public partial class form1 : Form
    {
        CppCLI m_GameEngine = null;
        bool m_APILoaded = false;

        bool m_TextBoxChanged = false;

        public form1()
        {
            InitializeComponent();

            m_GameEngine = new CppCLI();

            this.ResizeEnd += new EventHandler(form1_ResizeEnd);
            this.Resize += new EventHandler(form1_Resize);

            this.TextBoxToRender.MouseClick += new MouseEventHandler(TextBoxToRender_MouseClick);
        }

        public void GameLoop()
        {
            while (this.Created)
            {
                Run();
                Application.DoEvents();
            }
        }
        //This is our update/Renderloop
        private void Run()
        {
            if (m_APILoaded)
            {
                //Run the GameEngine for one frame
                m_GameEngine.ProcessFrame();
            }
        }

        void form1_Resize(object sender, EventArgs e)
        {
            //Hantera när maximize knappen trycks
            if (this.WindowState == FormWindowState.Maximized)
            {
                m_GameEngine.OnResize(RenderBox.Width, RenderBox.Height);
            }
            //När man återgår till "normal" state igen så hantera de också
            else if (this.WindowState == FormWindowState.Normal)
            {
                m_GameEngine.OnResize(RenderBox.Width, RenderBox.Height);
            }
        }

        void form1_ResizeEnd(object sender, EventArgs e)
        {
            m_GameEngine.OnResize(RenderBox.Width, RenderBox.Height);
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        void TextBoxToRender_MouseClick(object sender, MouseEventArgs e)
        {
            if (!m_TextBoxChanged)
            {
                TextBoxToRender.Text = "";
                m_TextBoxChanged = true;
            }
        }

        private void InitAPI_Click(object sender, EventArgs e)
        {
            if (apiToLoad.Text == "HGE")
            {
                m_GameEngine.Init(RenderBox.Handle, RenderBox.Width, RenderBox.Height);
                m_APILoaded = true;
            }
            else
            {
                MessageBox.Show("No api was selected or the api is not supported!!", "Warning", MessageBoxButtons.OK);
            }
        }

        private void PrintTextBoxText_Click(object sender, EventArgs e)
        {
            MessageBox.Show(m_GameEngine.ProcessText(TextBoxToRender.Text), "MessageBox", MessageBoxButtons.OK);
        }
    }
}
