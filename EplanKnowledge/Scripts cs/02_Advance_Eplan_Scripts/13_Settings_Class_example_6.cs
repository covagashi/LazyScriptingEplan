using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        Eplan.EplApi.Base.Settings oSettings =
            new Eplan.EplApi.Base.Settings();

        int intSetting = oSettings.GetNumericSetting(
            "USER.MF.PREVIEW.MINCOLWIDTH",
            0
            );

        MessageBox.Show("Minimum width of the tiles in the preview: "
            + intSetting.ToString());

        return;
    }

}