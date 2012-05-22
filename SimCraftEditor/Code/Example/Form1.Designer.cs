namespace Example
{
    partial class form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(form1));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.helpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.panel1 = new System.Windows.Forms.Panel();
            this.TreePanel = new System.Windows.Forms.Panel();
            this.TreeWood = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.TreeAge = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.HumanPanel = new System.Windows.Forms.Panel();
            this.label1 = new System.Windows.Forms.Label();
            this.HumanAge = new System.Windows.Forms.TextBox();
            this.HumanFemale = new System.Windows.Forms.RadioButton();
            this.HumanMale = new System.Windows.Forms.RadioButton();
            this.FoodBushPanel = new System.Windows.Forms.Panel();
            this.FoodBushFood = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.UnitList = new System.Windows.Forms.ComboBox();
            this.CreateUnitButton = new System.Windows.Forms.Button();
            this.toolStripContainer1 = new System.Windows.Forms.ToolStripContainer();
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.DeleteUnitButton = new System.Windows.Forms.ToolStripButton();
            this.RenderBox = new System.Windows.Forms.Panel();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.menuStrip1.SuspendLayout();
            this.panel1.SuspendLayout();
            this.TreePanel.SuspendLayout();
            this.HumanPanel.SuspendLayout();
            this.FoodBushPanel.SuspendLayout();
            this.toolStripContainer1.TopToolStripPanel.SuspendLayout();
            this.toolStripContainer1.SuspendLayout();
            this.toolStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.helpToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1361, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newToolStripMenuItem,
            this.openToolStripMenuItem,
            this.toolStripSeparator,
            this.saveToolStripMenuItem,
            this.saveAsToolStripMenuItem,
            this.toolStripSeparator2,
            this.exitToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // newToolStripMenuItem
            // 
            this.newToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.newToolStripMenuItem.Name = "newToolStripMenuItem";
            this.newToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
            this.newToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.newToolStripMenuItem.Text = "&New";
            this.newToolStripMenuItem.Click += new System.EventHandler(this.newToolStripMenuItem_Click);
            // 
            // openToolStripMenuItem
            // 
            this.openToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.openToolStripMenuItem.Name = "openToolStripMenuItem";
            this.openToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
            this.openToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.openToolStripMenuItem.Text = "&Open";
            this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // toolStripSeparator
            // 
            this.toolStripSeparator.Name = "toolStripSeparator";
            this.toolStripSeparator.Size = new System.Drawing.Size(143, 6);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.saveToolStripMenuItem.Text = "&Save";
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.saveToolStripMenuItem_Click);
            // 
            // saveAsToolStripMenuItem
            // 
            this.saveAsToolStripMenuItem.Name = "saveAsToolStripMenuItem";
            this.saveAsToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.saveAsToolStripMenuItem.Text = "Save &As";
            this.saveAsToolStripMenuItem.Click += new System.EventHandler(this.saveAsToolStripMenuItem_Click);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(143, 6);
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.exitToolStripMenuItem.Text = "E&xit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // helpToolStripMenuItem
            // 
            this.helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            this.helpToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.helpToolStripMenuItem.Text = "&Help";
            this.helpToolStripMenuItem.Click += new System.EventHandler(this.helpToolStripMenuItem_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.TreePanel);
            this.panel1.Controls.Add(this.HumanPanel);
            this.panel1.Controls.Add(this.FoodBushPanel);
            this.panel1.Controls.Add(this.UnitList);
            this.panel1.Controls.Add(this.CreateUnitButton);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Right;
            this.panel1.Location = new System.Drawing.Point(1161, 24);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(200, 719);
            this.panel1.TabIndex = 1;
            // 
            // TreePanel
            // 
            this.TreePanel.Controls.Add(this.TreeWood);
            this.TreePanel.Controls.Add(this.label3);
            this.TreePanel.Controls.Add(this.TreeAge);
            this.TreePanel.Controls.Add(this.label2);
            this.TreePanel.Location = new System.Drawing.Point(0, 28);
            this.TreePanel.Name = "TreePanel";
            this.TreePanel.Size = new System.Drawing.Size(200, 647);
            this.TreePanel.TabIndex = 4;
            this.TreePanel.Visible = false;
            // 
            // TreeWood
            // 
            this.TreeWood.Location = new System.Drawing.Point(72, 28);
            this.TreeWood.Name = "TreeWood";
            this.TreeWood.Size = new System.Drawing.Size(100, 20);
            this.TreeWood.TabIndex = 3;
            this.TreeWood.Text = "1000";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(16, 31);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(39, 13);
            this.label3.TabIndex = 2;
            this.label3.Text = "Wood:";
            // 
            // TreeAge
            // 
            this.TreeAge.Location = new System.Drawing.Point(72, 5);
            this.TreeAge.Name = "TreeAge";
            this.TreeAge.Size = new System.Drawing.Size(100, 20);
            this.TreeAge.TabIndex = 1;
            this.TreeAge.Text = "50";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(26, 8);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 13);
            this.label2.TabIndex = 0;
            this.label2.Text = "Age:";
            // 
            // HumanPanel
            // 
            this.HumanPanel.Controls.Add(this.label1);
            this.HumanPanel.Controls.Add(this.HumanAge);
            this.HumanPanel.Controls.Add(this.HumanFemale);
            this.HumanPanel.Controls.Add(this.HumanMale);
            this.HumanPanel.Location = new System.Drawing.Point(0, 31);
            this.HumanPanel.Name = "HumanPanel";
            this.HumanPanel.Size = new System.Drawing.Size(200, 647);
            this.HumanPanel.TabIndex = 2;
            this.HumanPanel.Visible = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(26, 31);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Age:";
            // 
            // HumanAge
            // 
            this.HumanAge.Location = new System.Drawing.Point(61, 28);
            this.HumanAge.Name = "HumanAge";
            this.HumanAge.Size = new System.Drawing.Size(89, 20);
            this.HumanAge.TabIndex = 2;
            this.HumanAge.Text = "20";
            // 
            // HumanFemale
            // 
            this.HumanFemale.AutoSize = true;
            this.HumanFemale.Location = new System.Drawing.Point(99, 4);
            this.HumanFemale.Name = "HumanFemale";
            this.HumanFemale.Size = new System.Drawing.Size(59, 17);
            this.HumanFemale.TabIndex = 1;
            this.HumanFemale.TabStop = true;
            this.HumanFemale.Text = "Female";
            this.HumanFemale.UseVisualStyleBackColor = true;
            // 
            // HumanMale
            // 
            this.HumanMale.AutoSize = true;
            this.HumanMale.Location = new System.Drawing.Point(7, 4);
            this.HumanMale.Name = "HumanMale";
            this.HumanMale.Size = new System.Drawing.Size(48, 17);
            this.HumanMale.TabIndex = 0;
            this.HumanMale.TabStop = true;
            this.HumanMale.Text = "Male";
            this.HumanMale.UseVisualStyleBackColor = true;
            // 
            // FoodBushPanel
            // 
            this.FoodBushPanel.Controls.Add(this.FoodBushFood);
            this.FoodBushPanel.Controls.Add(this.label4);
            this.FoodBushPanel.Location = new System.Drawing.Point(0, 31);
            this.FoodBushPanel.Name = "FoodBushPanel";
            this.FoodBushPanel.Size = new System.Drawing.Size(200, 641);
            this.FoodBushPanel.TabIndex = 4;
            this.FoodBushPanel.Visible = false;
            // 
            // FoodBushFood
            // 
            this.FoodBushFood.Location = new System.Drawing.Point(72, 15);
            this.FoodBushFood.Name = "FoodBushFood";
            this.FoodBushFood.Size = new System.Drawing.Size(100, 20);
            this.FoodBushFood.TabIndex = 1;
            this.FoodBushFood.Text = "1000";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(19, 18);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(34, 13);
            this.label4.TabIndex = 0;
            this.label4.Text = "Food:";
            // 
            // UnitList
            // 
            this.UnitList.FormattingEnabled = true;
            this.UnitList.Items.AddRange(new object[] {
            "Human",
            "Food Bush",
            "Tree",
            "Wolf"});
            this.UnitList.Location = new System.Drawing.Point(6, 4);
            this.UnitList.Name = "UnitList";
            this.UnitList.Size = new System.Drawing.Size(182, 21);
            this.UnitList.TabIndex = 1;
            this.UnitList.Text = "Choose Unit Type";
            this.UnitList.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
            // 
            // CreateUnitButton
            // 
            this.CreateUnitButton.Location = new System.Drawing.Point(6, 684);
            this.CreateUnitButton.Name = "CreateUnitButton";
            this.CreateUnitButton.Size = new System.Drawing.Size(182, 23);
            this.CreateUnitButton.TabIndex = 0;
            this.CreateUnitButton.Text = "Create Unit";
            this.CreateUnitButton.UseVisualStyleBackColor = true;
            this.CreateUnitButton.Click += new System.EventHandler(this.CreateUnitButton_Click);
            // 
            // toolStripContainer1
            // 
            this.toolStripContainer1.BottomToolStripPanelVisible = false;
            // 
            // toolStripContainer1.ContentPanel
            // 
            this.toolStripContainer1.ContentPanel.Size = new System.Drawing.Size(1161, 0);
            this.toolStripContainer1.Dock = System.Windows.Forms.DockStyle.Top;
            this.toolStripContainer1.LeftToolStripPanelVisible = false;
            this.toolStripContainer1.Location = new System.Drawing.Point(0, 24);
            this.toolStripContainer1.Name = "toolStripContainer1";
            this.toolStripContainer1.RightToolStripPanelVisible = false;
            this.toolStripContainer1.Size = new System.Drawing.Size(1161, 25);
            this.toolStripContainer1.TabIndex = 2;
            this.toolStripContainer1.Text = "toolStripContainer1";
            // 
            // toolStripContainer1.TopToolStripPanel
            // 
            this.toolStripContainer1.TopToolStripPanel.Controls.Add(this.toolStrip1);
            // 
            // toolStrip1
            // 
            this.toolStrip1.Dock = System.Windows.Forms.DockStyle.None;
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.DeleteUnitButton});
            this.toolStrip1.Location = new System.Drawing.Point(3, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(171, 25);
            this.toolStrip1.TabIndex = 0;
            // 
            // DeleteUnitButton
            // 
            this.DeleteUnitButton.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
            this.DeleteUnitButton.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.DeleteUnitButton.Image = ((System.Drawing.Image)(resources.GetObject("DeleteUnitButton.Image")));
            this.DeleteUnitButton.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.DeleteUnitButton.Name = "DeleteUnitButton";
            this.DeleteUnitButton.Size = new System.Drawing.Size(159, 22);
            this.DeleteUnitButton.Text = "Delete Unit Closest to Arrow";
            this.DeleteUnitButton.Click += new System.EventHandler(this.DeleteUnitButton_Click);
            // 
            // RenderBox
            // 
            this.RenderBox.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.RenderBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.RenderBox.Location = new System.Drawing.Point(0, 49);
            this.RenderBox.Name = "RenderBox";
            this.RenderBox.Size = new System.Drawing.Size(1161, 694);
            this.RenderBox.TabIndex = 3;
            // 
            // statusStrip1
            // 
            this.statusStrip1.Location = new System.Drawing.Point(0, 721);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(1161, 22);
            this.statusStrip1.TabIndex = 4;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1361, 743);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.RenderBox);
            this.Controls.Add(this.toolStripContainer1);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.MinimumSize = new System.Drawing.Size(500, 290);
            this.Name = "form1";
            this.Text = "SimCraft Level-Editor";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.form1_FormClosing);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.TreePanel.ResumeLayout(false);
            this.TreePanel.PerformLayout();
            this.HumanPanel.ResumeLayout(false);
            this.HumanPanel.PerformLayout();
            this.FoodBushPanel.ResumeLayout(false);
            this.FoodBushPanel.PerformLayout();
            this.toolStripContainer1.TopToolStripPanel.ResumeLayout(false);
            this.toolStripContainer1.TopToolStripPanel.PerformLayout();
            this.toolStripContainer1.ResumeLayout(false);
            this.toolStripContainer1.PerformLayout();
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem newToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveAsToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem helpToolStripMenuItem;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.ToolStripContainer toolStripContainer1;
        private System.Windows.Forms.Panel RenderBox;
        private System.Windows.Forms.Button CreateUnitButton;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ComboBox UnitList;
        private System.Windows.Forms.Panel HumanPanel;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox HumanAge;
        private System.Windows.Forms.RadioButton HumanFemale;
        private System.Windows.Forms.RadioButton HumanMale;
        private System.Windows.Forms.Panel TreePanel;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox TreeWood;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox TreeAge;
        private System.Windows.Forms.Panel FoodBushPanel;
        private System.Windows.Forms.TextBox FoodBushFood;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripButton DeleteUnitButton;
    }
}

