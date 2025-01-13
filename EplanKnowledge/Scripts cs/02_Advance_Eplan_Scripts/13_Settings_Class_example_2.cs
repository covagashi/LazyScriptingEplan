using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        Eplan.EplApi.Base.Settings oSettings =
            new Eplan.EplApi.Base.Settings();

        oSettings.SetBoolSetting(
            "USER.EnfMVC.ContextMenuSetting.ShowExtended",
            true,
            0
            );

        MessageBox.Show(
            "Setting has been activated. EPLAN restart required."
            );

        return;
    }

}