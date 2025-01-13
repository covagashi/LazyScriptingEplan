using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        CommandLineInterpreter oCLI = new CommandLineInterpreter();
        ActionCallingContext acc = new ActionCallingContext();

        acc.AddParameter("PropertyId", "10013");
        acc.AddParameter("PropertyIndex", "0");
        acc.AddParameter("PropertyValue", "23542");

        oCLI.Execute("XEsSetProjectPropertyAction", acc);

        MessageBox.Show("Action ausgeführt.");

        return;
    }
}
