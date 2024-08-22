using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
public class Script
{
  [Start]
  public void Action()
  {
    InsertMacro(@"C:\Test\Test.ema", "/2");
  }
  private void InsertMacro(string macroFileName, string pageName)
  {
    Edit(pageName);
    Parallel.Invoke(() =>
                      InsertMacro(macroFileName),
                    KeyPress);
  }
  private static void InsertMacro(string macroFileName)
  {
    ActionCallingContext acc = new ActionCallingContext();
    acc.AddParameter("Name", "XMIaInsertMacro");
    acc.AddParameter("filename", macroFileName);
    acc.AddParameter("variant", "0");
    CommandLineInterpreter cli = new CommandLineInterpreter();
    cli.Execute("XGedStartInteractionAction", acc);
  }
  private static void Edit(string pageName)
  {
    ActionCallingContext acc = new ActionCallingContext();
    acc.AddParameter("PAGENAME", pageName); // Full page name
    acc.AddParameter("X", "100");
    acc.AddParameter("Y", "100");
    CommandLineInterpreter cli = new CommandLineInterpreter();
    cli.Execute("edit", acc);
  }
  private void KeyPress()
  {
    Thread.Sleep(1000);
    SendKeys.SendWait("{ENTER}");
  }
}