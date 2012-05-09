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

            //this.TextBoxToRender.MouseClick += new MouseEventHandler(TextBoxToRender_MouseClick);
            this.RenderBox.MouseDown += new MouseEventHandler(RenderBox_MouseDown);
            this.RenderBox.MouseUp += new MouseEventHandler(RenderBox_MouseUp);
            //this.RenderBox.PreviewKeyDown += new KeyEventHandler(

            this.KeyPreview = true;
            this.KeyDown += new KeyEventHandler(RenderBox_KeyDown);
            this.KeyUp += new KeyEventHandler(RenderBox_KeyUp);
            this.KeyPress += new KeyPressEventHandler(RenderBox_KeyPress);

        }

        void RenderBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (MousePosition.X > this.PointToScreen(RenderBox.Location).X &&
                MousePosition.X < this.PointToScreen(RenderBox.Location).X + RenderBox.Size.Width)
            {
                if (MousePosition.Y > this.PointToScreen(RenderBox.Location).Y &&
                        MousePosition.Y < this.PointToScreen(RenderBox.Location).Y + RenderBox.Size.Height)
                {
                    
                    m_GameEngine.KeyDown((int)e.KeyCode);
                    
                }
            }
           
        }

        void RenderBox_KeyUp(Object sender, KeyEventArgs e)
        {
            /*
            if (MousePosition.X > this.PointToScreen(RenderBox.Location).X &&
                MousePosition.X < this.PointToScreen(RenderBox.Location).X + RenderBox.Size.Width)
            {
                if (MousePosition.Y > this.PointToScreen(RenderBox.Location).Y &&
                        MousePosition.Y < this.PointToScreen(RenderBox.Location).Y + RenderBox.Size.Height)
                {*/
                    m_GameEngine.KeyUp((int)e.KeyCode);
               // }
          //  }
        }
        void RenderBox_KeyPress(Object sender, KeyPressEventArgs e)
        {
            if (MousePosition.X > this.PointToScreen(RenderBox.Location).X &&
                MousePosition.X < this.PointToScreen(RenderBox.Location).X + RenderBox.Size.Width)
            {
                if (MousePosition.Y > this.PointToScreen(RenderBox.Location).Y &&
                        MousePosition.Y < this.PointToScreen(RenderBox.Location).Y + RenderBox.Size.Height)
                {
                    e.Handled = true;
                }
            }
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
                m_TextBoxChanged = true;
            }
        }

        void RenderBox_MouseDown(object sender, MouseEventArgs e)
        {
            
            int button = 0;
            switch (e.Button)
            {
                case MouseButtons.Left:
                    button = 1;
                    break;
                case MouseButtons.Right:
                    button = 2;
                    break;
            }
            m_GameEngine.MouseDown(button);
        }
        void RenderBox_MouseUp(object sender, MouseEventArgs e)
        {
            int button = 0;
            switch (e.Button)
            {
                case MouseButtons.Left:
                    button = 1;
                    break;
                case MouseButtons.Right:
                    button = 2;
                    break;
            }
            m_GameEngine.MouseUp(button);
        }


        private void InitAPI_Click(object sender, EventArgs e)
        {
            if (apiToLoad.Text == "MaloWEngine")
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
            
        }
    }
}
