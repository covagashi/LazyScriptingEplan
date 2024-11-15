using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;

public class ProjectDetailUpdater
{
    [Start]
    public void Function()
    {
        CommandLineInterpreter oCLI = new CommandLineInterpreter();
        ActionCallingContext acc = new ActionCallingContext();

        // Project path with proper string literal formatting
        acc.AddParameter("PROJECTNAME", @"C:\Projects\EPLAN\EPLAN_Sample_Project.elk");
        
        // Update settings
        acc.AddParameter("UpdateMacros", "1");
        acc.AddParameter("UpdateIdentifier", "1");

        // Execute detail update action
        oCLI.Execute("XPlaUpdateDetailAction", acc);

        return;
    }
}