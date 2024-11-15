using System.Windows.Forms;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        string strProjectname = PathMap.SubstitutePath("$(PROJECTNAME)"); // The symbol $ in Eplan its only used for path variables
        
        MessageBox.Show(strProjectname);

        return;
    }
}



