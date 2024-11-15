using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        CommandLineInterpreter oCLI = new CommandLineInterpreter();

        oCLI.Execute("gedRedraw");
        oCLI.Execute("UpdateSegmentsFilling");
        oCLI.Execute("XGedClosePage");

        return;
    }
}



