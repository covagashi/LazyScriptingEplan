using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        CommandLineInterpreter oCLI = new CommandLineInterpreter();

        Progress oProgress = new Progress("EnhancedProgress");
        oProgress.SetAllowCancel(false);
        oProgress.ShowImmediately();

        oProgress.BeginPart(33, "Part 1");
        oCLI.Execute("generate /TYPE:CONNECTIONS");
        oProgress.EndPart();

        oProgress.BeginPart(33, "Part 2");
        oCLI.Execute("reports");
        oProgress.EndPart();

        oProgress.BeginPart(33, "Part 3");
        oCLI.Execute("compress /FILTERSCHEME:Standard");
        oProgress.EndPart();

        oProgress.EndPart(true);

        return;
    }
}



