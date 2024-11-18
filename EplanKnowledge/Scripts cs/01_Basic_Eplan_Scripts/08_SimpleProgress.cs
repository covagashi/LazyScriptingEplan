using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;
using System.Threading;

public class Class
{
    [Start]
    public void Function()
    {
        Progress oProgress = new Progress("SimpleProgress");
        oProgress.SetAllowCancel(true);
        oProgress.SetAskOnCancel(true);
        oProgress.SetNeededSteps(3);
        oProgress.SetTitle("My Progress Bar");
        oProgress.ShowImmediately();

        if (!oProgress.Canceled())
        {
            oProgress.SetActionText("Step 1");
            oProgress.SetTitle("Title line 1");
            oProgress.Step(1);

            Thread.Sleep(1000);
        }

        if (!oProgress.Canceled())
        {
            oProgress.SetActionText("Step 2");
            oProgress.SetTitle("Title line 2");
            oProgress.Step(1);

            Thread.Sleep(1000);
        }

        if (!oProgress.Canceled())
        {
            oProgress.SetActionText("Step 3");
            oProgress.SetTitle("Title line 3");
            oProgress.Step(1);

            Thread.Sleep(1000);
        }

        oProgress.EndPart(true);

        return;
    }
}



