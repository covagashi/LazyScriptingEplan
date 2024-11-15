using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [DeclareRegister]
    public void Register()
    {
        MessageBox.Show("Script loaded.");

        return;
    }

    [DeclareUnregister]
    public void UnRegister()
    {
        MessageBox.Show("Unload script.");

        return;
    }
}



