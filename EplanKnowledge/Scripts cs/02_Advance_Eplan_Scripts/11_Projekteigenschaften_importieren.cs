using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        string strProjects =
            PathMap.SubstitutePath("$(MD_PROJECTS)");
        string strFilename = string.Empty;

        OpenFileDialog ofd = new OpenFileDialog();
        ofd.Filter = "ProjectInfo.xml|ProjectInfo.xml";
        ofd.InitialDirectory = strProjects;
        ofd.Title = "Projekteigenschaften auswählen:";
        ofd.ValidateNames = true;

        if (ofd.ShowDialog() == DialogResult.OK)
        {
            strFilename = ofd.FileName;

            Progress oProgress = new Progress("SimpleProgress");
            oProgress.SetAllowCancel(false);
            oProgress.BeginPart(100, "");
            oProgress.SetTitle("Projekteigenschaften importieren");
            oProgress.ShowImmediately();

            CommandLineInterpreter oCLI = new CommandLineInterpreter();
            ActionCallingContext cc = new ActionCallingContext();

            cc.AddParameter("TYPE", "READPROJECTINFO");
            cc.AddParameter("FILENAME", strFilename);
            oCLI.Execute("projectmanagement", cc);

            oProgress.EndPart(true);

            oCLI.Execute("XPrjActionPropertiesEdit");
        }

        return;
    }
}

