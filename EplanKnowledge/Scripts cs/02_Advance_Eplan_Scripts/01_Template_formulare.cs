using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public partial class frmTemplate : System.Windows.Forms.Form
{
    #region Windows Form Designer generated code

    /// <summary>
    /// Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">True if managed resources
    /// should be disposed; otherwise false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    /// <summary>
    /// Required method for Designer support.
    /// The contents of this method should not be modified
    /// with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.SuspendLayout();
        // 
        // frmTemplate
        // 
        this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(292, 273);
        this.Name = "frmTemplate";
        this.StartPosition = 
            System.Windows.Forms.FormStartPosition.CenterScreen;
        this.Text = "Template";
        this.ResumeLayout(false);
    }

    public frmTemplate()
    {
        InitializeComponent();
    }

    #endregion

    [Start]
    public void Function()
    {
        frmTemplate frm = new frmTemplate();
        frm.ShowDialog();

        return;
    }
}