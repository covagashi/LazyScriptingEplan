using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        Eplan.EplApi.Base.Settings oSettings =
            new Eplan.EplApi.Base.Settings();

        oSettings.SetStringSetting(
            "USER.TrDMProject.UserData.Identification",
            "TEST",
            0
            );

        MessageBox.Show("Setting has been set.");

        return;
    }

}