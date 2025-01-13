using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        Eplan.EplApi.Base.Settings oSettings =
            new Eplan.EplApi.Base.Settings();

        oSettings.SetNumericSetting(
            "USER.SYSTEM.GUI.LAST_PROJECTS_COUNT",
            11,
            0
            );

        MessageBox.Show("Setting has been set.");

        return;
    }

}