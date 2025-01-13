using System;
using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [DeclareAction("ImportSettings")]
    public void Function(int SET)
    {
        try
        {
            string strScripts =
                PathMap.SubstitutePath("$(MD_SCRIPTS)" + @"\");
            string strProject = PathMap.SubstitutePath("$(P)");
            string strMessage = string.Empty;

            CommandLineInterpreter oCLI = new CommandLineInterpreter();
            ActionCallingContext acc = new ActionCallingContext();
            acc.AddParameter("Project", strProject);

            switch (SET)
            {
                case 1:
                    strMessage = "[As drawn]";
                    acc.AddParameter("XMLFile", strScripts + @"1.xml");
                    break;

                case 2:
                    strMessage = "[As a point]";
                    acc.AddParameter("XMLFile", strScripts + @"2.xml");
                    break;

                case 3:
                    strMessage = "[With target setting]";
                    acc.AddParameter("XMLFile", strScripts + @"3.xml");
                    break;

                default:
                    MessageBox.Show("Parameter not known",
                        "Error", MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                    return;
            }

            oCLI.Execute("XSettingsImport", acc);

            MessageBox.Show("Settings have been imported.\n"
                + strMessage, "Information",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);

        }
        catch (Exception ex)
        {
            MessageBox.Show(ex.Message, "Error",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);
        }

        return;
    }

}