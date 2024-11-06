using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class FClass
{
    [DeclareAction("Actionname")]
    public void Function()
    {
        MessageBox.Show("Hello world called by action");

        return;
    }
}



