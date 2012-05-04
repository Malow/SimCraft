using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace Example
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new form1());

            form1 form = new form1();
            form.Show();
            form.GameLoop();
        }
    }
}
