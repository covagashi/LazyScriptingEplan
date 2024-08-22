// ExecuteEplanAction.cs
//
// Mit diesem Script kann eine beliebige Action in EPLAN ausgeführt werden.
//
// Ursprung: https://suplanus.de/executeeplanaction/
//
// Copyright by Frank Schöneck, 2011-2021
// letzte Änderung:
// V1.0.0, 18.08.2011, Johann Weiher, Projektbeginn
// V2.0.0, 04.04.2017, Frank Schöneck, Um das abspeichern der zuletzt verwendeten Action erweitert,
//                                     um den Aufruf des ActionList-Dialoges erweitert.
// V2.1.0, 11.04.2019, Frank Schöneck, Mit der ENTER Taste kann nun die Eingabe abgeschlossen werden.
// V3.0.0, 05.11.2020, Frank Schöneck, Die Eingangezeile ist nun eine Kombobox und speichert die letzten 5 Eingaben.
// V4.0.0, 17.09.2021, Frank Schöneck, Angepasst an die Ribbon-Technik der EPLAN Plattform 2022.
//
// für Eplan Electric P8, ab V2022

/*
The following compiler directive is necessary to enable editing scripts
within Visual Studio.
It requires that the "Conditional compilation symbol" SCRIPTENV be defined 
in the Visual Studio project properties
This is because EPLAN's internal scripting engine already adds "using directives"
when you load the script in EPLAN. Having them twice would cause errors.
*/

#if SCRIPTENV
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;
using Eplan.EplApi.Gui;
#endif

/*
On the other hand, some namespaces are not automatically added by EPLAN when
you load a script. Those have to be outside of the previous conditional compiler directive
*/

using System.Drawing;
using System.Windows.Forms;

public partial class frmExecuteEplanAction : System.Windows.Forms.Form
{
	private CommandLineInterpreter oCLI = new CommandLineInterpreter();
	private Button btnCancel;
	private Button btnOk;
	private Label label1;
	private Button btnMore;
	private ComboBox comboBoxAction;

	#region Vom Windows Form-Designer generierter Code

	/// <summary>
	/// Erforderliche Designervariable.
	/// </summary>
	private System.ComponentModel.IContainer components = null;

	/// <summary>
	/// Verwendete Ressourcen bereinigen.
	/// </summary>
	/// <param name="disposing">True, wenn verwaltete Ressourcen
	/// gelöscht werden sollen; andernfalls False.</param>
	protected override void Dispose(bool disposing)
	{
		if (disposing && (components != null))
		{
			components.Dispose();
		}
		base.Dispose(disposing);
	}

	/// <summary>
	/// Erforderliche Methode für die Designerunterstützung.
	/// Der Inhalt der Methode darf nicht mit dem Code-Editor
	/// geändert werden.
	/// </summary>
	private void InitializeComponent()
	{
		this.btnCancel = new System.Windows.Forms.Button();
		this.btnOk = new System.Windows.Forms.Button();
		this.label1 = new System.Windows.Forms.Label();
		this.btnMore = new System.Windows.Forms.Button();
		this.comboBoxAction = new System.Windows.Forms.ComboBox();
		this.SuspendLayout();
		// 
		// btnCancel
		// 
		this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
		this.btnCancel.Location = new System.Drawing.Point(541, 153);
		this.btnCancel.Margin = new System.Windows.Forms.Padding(6);
		this.btnCancel.Name = "btnCancel";
		this.btnCancel.Size = new System.Drawing.Size(220, 50);
		this.btnCancel.TabIndex = 1;
		this.btnCancel.Text = "Cancelar";
		this.btnCancel.UseVisualStyleBackColor = true;
		this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
		// 
		// btnOk
		// 
		this.btnOk.Enabled = false;
		this.btnOk.Location = new System.Drawing.Point(290, 153);
		this.btnOk.Margin = new System.Windows.Forms.Padding(6);
		this.btnOk.Name = "btnOk";
		this.btnOk.Size = new System.Drawing.Size(220, 50);
		this.btnOk.TabIndex = 0;
		this.btnOk.Text = "OK";
		this.btnOk.UseVisualStyleBackColor = true;
		this.btnOk.Click += new System.EventHandler(this.btnOk_Click);
		// 
		// label1
		// 
		this.label1.AutoSize = true;
		this.label1.Location = new System.Drawing.Point(22, 37);
		this.label1.Margin = new System.Windows.Forms.Padding(6, 0, 6, 0);
		this.label1.Name = "label1";
		this.label1.Size = new System.Drawing.Size(123, 25);
		this.label1.TabIndex = 2;
		this.label1.Text = "Línea de comando:";
		// 
		// btnMore
		// 
		this.btnMore.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold);
		this.btnMore.Location = new System.Drawing.Point(709, 64);
		this.btnMore.Margin = new System.Windows.Forms.Padding(6);
		this.btnMore.Name = "btnMore";
		this.btnMore.Size = new System.Drawing.Size(50, 42);
		this.btnMore.TabIndex = 4;
		this.btnMore.Text = "...";
		this.btnMore.UseVisualStyleBackColor = true;
		this.btnMore.Click += new System.EventHandler(this.btnMore_Click);
		// 
		// comboBoxAction
		// 
		this.comboBoxAction.Location = new System.Drawing.Point(12, 70);
		this.comboBoxAction.MaxDropDownItems = 5;
		this.comboBoxAction.Name = "comboBoxAction";
		this.comboBoxAction.Size = new System.Drawing.Size(675, 32);
		this.comboBoxAction.TabIndex = 3;
		this.comboBoxAction.TextChanged += new System.EventHandler(this.comboBoxAction_TextChanged);
		this.comboBoxAction.KeyDown += new System.Windows.Forms.KeyEventHandler(this.comboBoxAction_KeyDown);
		// 
		// frmExecuteEplanAction
		// 
		this.AcceptButton = this.btnOk;
		this.AutoScaleDimensions = new System.Drawing.SizeF(11F, 24F);
		this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
		this.CancelButton = this.btnCancel;
		this.ClientSize = new System.Drawing.Size(783, 225);
		this.Controls.Add(this.comboBoxAction);
		this.Controls.Add(this.btnMore);
		this.Controls.Add(this.label1);
		this.Controls.Add(this.btnOk);
		this.Controls.Add(this.btnCancel);
		this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
		this.Margin = new System.Windows.Forms.Padding(6);
		this.MaximizeBox = false;
		this.MinimizeBox = false;
		this.Name = "frmExecuteEplanAction";
		this.ShowInTaskbar = false;
		this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
		this.Text = "Eplan Ejecutar acción";
		this.Load += new System.EventHandler(this.frmExecuteEplanAction_Load);
		this.ResumeLayout(false);
		this.PerformLayout();

	}

	public frmExecuteEplanAction()
	{
		InitializeComponent();
	}

	#endregion

	string m_TabName = "Herramientas";
	string m_commandGroupName = "Extensiones";
	string m_commandName = "EPLAN Action realizar...";

	[DeclareRegister]
	public void registerRibbonItems()
	{
		var newTab = new Eplan.EplApi.Gui.RibbonBar().GetTab(m_TabName);
		var commandGroup = newTab.CommandGroups.FirstOrDefault(item => item.Name == m_commandGroupName);
		if (commandGroup == null) //CommandGroup aún no existe, luego crea uno nuevo
		{
			commandGroup = newTab.AddCommandGroup(m_commandGroupName);
		}
		var command = commandGroup.AddCommand(m_commandName, "ExecuteEplanAction", Eplan.EplApi.Gui.CommandIcon.Application);
		command.TooltipText = m_commandName;
		command.Description = "Avanzado EPLAN Action realizar";
	}

	[DeclareUnregister]
	public void unRegisterRibbonItems()
	{
		//Command eliminar
		var vTab = new Eplan.EplApi.Gui.RibbonBar().Tabs.FirstOrDefault(item => item.Name == m_TabName);
		if (vTab != null)
		{
			var commandGroup = vTab.CommandGroups.FirstOrDefault(item => item.Name == m_commandGroupName);
			if (commandGroup != null)
			{
				var command = commandGroup.Commands.Values.FirstOrDefault(item => item.Text == m_commandName);
				if (command != null)
				{
					command.Remove();
				}
				//Si CommandGroup está vacío, elimínelo también
				if (commandGroup.Commands.Count == 0)
				{
					commandGroup.Remove();
				}
			}
		}
		SettingsDelete();
	}

	[Start]
	[DeclareAction("ExecuteEplanAction")]
	public void Function()
	{
		frmExecuteEplanAction frm = new frmExecuteEplanAction();
		frm.ShowDialog();

		return;
	}

	private void btnCancel_Click(object sender, System.EventArgs e)
	{
		this.Close();

		return;
	}

	private void frmExecuteEplanAction_Load(object sender, System.EventArgs e)
	{
		//Lea el nombre de la última acción en la configuración.
		Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();
		if (oSettings.ExistSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME"))
		{
			//Kombobox vacío
			comboBoxAction.Items.Clear();
			comboBoxAction.IntegralHeight = false;

			//Llenar cuadro combinado
			int countIndex = oSettings.GetCountOfValues("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME");
			for (int index = 0; index < countIndex; index++)
			{
				comboBoxAction.Items.Add(oSettings.GetStringSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME", index));
			}

			comboBoxAction.SelectedIndex = 0; //Se muestra la primera entrada
		}

		comboBoxAction.Select();

		return;
	}

	private void btnOk_Click(object sender, System.EventArgs e)
	{
		//Agregar acción a la lista
		int index = comboBoxAction.FindString(comboBoxAction.Text); //La acción aún no está presente en el cuadro combinado
		if (index < 0)
		{
			comboBoxAction.Items.Insert(0, comboBoxAction.Text);
		}

		//Action realizar
		oCLI.Execute(comboBoxAction.Text);

		//Action ahorrar
		SettingsWrite();

		this.Close();

		return;
	}


	public void SettingsWrite()
	{
		//Guardar acción en Configuración
		Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();
		if (!oSettings.ExistSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME"))
		{
			oSettings.AddStringSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME",
				new string[] { },
				new string[] { },
				Eplan.EplApi.Base.ISettings.CreationFlag.Insert);
		}

		int index = 0;
		foreach (string action in comboBoxAction.Items)
		{
			if (index < 5) // max. 5 Entradas
			{
				oSettings.SetStringSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME", action, index);
			}
			index++;
		}
	}

	public void SettingsDelete()
	{
		//Settings borrar
		Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();
		if (oSettings.ExistSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME"))
		{
			oSettings.DeleteSetting("USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME");
			MessageBox.Show("los ajustes 'USER.SCRIPTS.EXECUTEEPLANACTION.ACTIONNAME' fueron eliminados.", "ExecuteEplanAction, Eliminar configuración", MessageBoxButtons.OK, MessageBoxIcon.Information);
		}
		else
		{
			MessageBox.Show("¡No se encontraron los ajustes!", "ExecuteEplanAction, Eliminar configuración", MessageBoxButtons.OK, MessageBoxIcon.Warning);
		}
	}

	private void btnMore_Click(object sender, System.EventArgs e)
	{
		//Action ausführen
		ActionCallingContext acc = new ActionCallingContext();
		CommandLineInterpreter oCLI = new CommandLineInterpreter();

		string sAktion = string.Empty;

		acc.AddParameter("DialogName", "XSDActionListDialog");
		oCLI.Execute("GfDialogManagerDoModal", acc);
		acc.GetParameter("ACTION", ref sAktion);

		comboBoxAction.Text = sAktion.Trim();

		return;
	}

	private void comboBoxAction_TextChanged(object sender, System.EventArgs e)
	{
		if (comboBoxAction.Text.Length > 0)
		{
			bool bRet = oCLI.IsExecutable(comboBoxAction.Text);
			if (bRet)
			{
				comboBoxAction.BackColor = Color.LightGreen;
				btnOk.Enabled = true;
			}
			else
			{
				comboBoxAction.BackColor = Color.LightSalmon;
				btnOk.Enabled = false;
			}
		}
		else
		{
			comboBoxAction.BackColor = Color.White;
		}

		return;

	}

	private void comboBoxAction_KeyDown(object sender, KeyEventArgs e)
	{
		if (e.KeyCode == Keys.Enter)
		{
			btnOk.PerformClick();
		}
	}

}

