using System;
using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class InterfazUsuarioSimple
{
    [Start]
    public void MostrarFormulario()
    {
        Form formulario = new Form();
        formulario.Text = "Mi Formulario EPLAN";
        formulario.Size = new System.Drawing.Size(300, 200);

        Button boton = new Button();
        boton.Text = "Haz clic aquí";
        boton.Location = new System.Drawing.Point(100, 50);
        boton.Click += (sender, e) => MessageBox.Show("¡Botón clicado!");

        formulario.Controls.Add(boton);
        formulario.ShowDialog();
    }
}