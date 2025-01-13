using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        Eplan.EplApi.Base.Settings oSettings =
            new Eplan.EplApi.Base.Settings();

        string strName = oSettings.GetStringSetting(
            "USER.TrDMProject.UserData.Longname",
            0
            );

        MessageBox.Show("Hello " + strName + "!");

        return;
    }
}