using System;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;
class Program
{
    [Start]
    public void Action()
    {
        // Get selected pages
        var pages = GetPages();
        // Setup progressbar
        Progress progress = new Progress("EnhancedProgress");
        progress.SetTitle("Do Something with pages");
        progress.SetAllowCancel(true);
        progress.ShowImmediately();
        progress.SetNeededSteps(pages.Length + 1);
        try
        {
            // Do something with pages
            foreach (var page in pages)
            {
                progress.SetActionText(page);
                progress.Step(1);
                SelectPage(page);
            }
        }
        catch (Exception exception)
        {
            MessageBox.Show(exception.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
        finally
        {
            progress.EndPart(true);
        }
    }
    private static string[] GetPages()
    {
        ActionCallingContext oACC = new ActionCallingContext();
        string pagesString = string.Empty;
        oACC.AddParameter("TYPE", "PAGES");
        new CommandLineInterpreter().Execute("selectionset", oACC);
        oACC.GetParameter("PAGES", ref pagesString);
        string[] pages = pagesString.Split(';');
        return pages;
    }
    private void SelectPage(string page)
    {
        ActionCallingContext oACC = new ActionCallingContext();
        CommandLineInterpreter oCLI = new CommandLineInterpreter();
        oACC.AddParameter("PAGENAME", page);
        oCLI.Execute("edit", oACC);
        oACC.AddParameter("PropertyId", "11006");
        oCLI.Execute("XEsGetPagePropertyAction", oACC);
        string propertyValue = "";
        oACC.GetParameter("PropertyValue", ref propertyValue);        

        if (string.Equals(propertyValue, "7", StringComparison.OrdinalIgnoreCase))
        {
            using (var qm = new QuietModeStep(QuietModes.ShowNoDialogs))
            {
                new CommandLineInterpreter().Execute("XPmExternalDeletePages");
            }
        }
        oCLI.Execute("XGedClosePage");
    }
}










