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

        bool changeHasBeenMade = false;

        bool m_TextBoxChanged = false;

        string filePath = "";


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

            this.InitEngine();
        }

        void RenderBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (MousePosition.X > this.PointToScreen(RenderBox.Location).X &&
                MousePosition.X < this.PointToScreen(RenderBox.Location).X + RenderBox.Size.Width)
            {
                if (MousePosition.Y > this.PointToScreen(RenderBox.Location).Y &&
                        MousePosition.Y < this.PointToScreen(RenderBox.Location).Y + RenderBox.Size.Height)
                {
                    e.Handled = true;
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
            if (this.changeHasBeenMade)
                if (MessageBox.Show("Your map has not beed saved, do you wish to save?", "Do you wish to Save?", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    this.Save();
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

        void InitEngine()
        {
            m_GameEngine.Init(RenderBox.Handle, RenderBox.Width, RenderBox.Height);
            m_APILoaded = true;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            HumanPanel.Hide();
            FoodBushPanel.Hide();
            TreePanel.Hide();

            // Save the selected employee's name, because we will remove
            // the employee's name from the list.
            string unit = (string)UnitList.SelectedItem;
            if (unit == "Human")
                HumanPanel.Show();
            else if (unit == "Tree")
                TreePanel.Show();
            else if (unit ==  "Food Bush")
                FoodBushPanel.Show();
        }

        private void CreateUnitButton_Click(object sender, EventArgs e)
        {
            HumanPanel.Hide();
            FoodBushPanel.Hide();
            TreePanel.Hide();

            // Save the selected employee's name, because we will remove
            // the employee's name from the list.
            string unit = (string)UnitList.SelectedItem;
            if (unit == "Human")
                m_GameEngine.CreateHuman(HumanMale.Checked, Convert.ToInt32(HumanAge.Text));
            else if (unit == "Tree")
                m_GameEngine.CreateTree(Convert.ToInt32(TreeAge.Text), Convert.ToInt32(TreeWood.Text));
            else if (unit == "Food Bush")
                m_GameEngine.CreateFoodBush(Convert.ToInt32(FoodBushFood.Text));

            this.changeHasBeenMade = true;
        }

        private void DeleteUnitButton_Click(object sender, EventArgs e)
        {
            m_GameEngine.DeleteUnitClosestToArrow();
            this.changeHasBeenMade = true;
        }

        private void helpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Mouseover the 3D Scene and use the arrow-keys to move around the arrow, " +
                "and use WASD and mouse-buttons to move the camera and to zoom the camera. " + '\n' + '\n' + 
                "Choose unit type in the list to the right and when you're done changing " +
                "the settings press Create Unit to place the unit on the arrow. " + '\n' + '\n' + 
                "To delete a unit go close to it with the arrow and then press on the " + 
                "Delete Unit Closest to Arrow button in the top.", "Instructions", MessageBoxButtons.OK);
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (this.changeHasBeenMade)
                if (MessageBox.Show("Your map has not beed saved, do you wish to save?", "Do you wish to Save?", MessageBoxButtons.YesNo) == DialogResult.Yes) 
                    this.Save();

            this.changeHasBeenMade = false;

            this.m_GameEngine.ResetScene();
            this.filePath = "";
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (this.changeHasBeenMade)
                if (MessageBox.Show("Your map has not beed saved, do you wish to save?", "Do you wish to Save?", MessageBoxButtons.YesNo) == DialogResult.Yes)
                    this.Save();

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Title = "Load a map";
            ofd.ShowDialog();

            if (ofd.FileName != "")
            {
                this.m_GameEngine.LoadFromPath(ofd.FileName);
                this.filePath = ofd.FileName;
                this.changeHasBeenMade = false;
            }
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Save();
        }

        private void saveAsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.SaveAs();
        }

        void Save()
        {
            if (filePath == "")
                this.SaveAs();
            else
            {
                this.m_GameEngine.SaveToPath(this.filePath + ".txt");
                this.changeHasBeenMade = false;
            }
        }

        void SaveAs()
        {
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Title = "Save a map";
            sfd.ShowDialog();

            if (sfd.FileName != "")
            {
                this.m_GameEngine.SaveToPath(sfd.FileName + ".txt");
                this.filePath = sfd.FileName;
                this.changeHasBeenMade = false;
            }
        }
    }
}
