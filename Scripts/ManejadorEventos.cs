using System.Windows.Forms;
using Eplan.EplApi.Scripting;

public class ManejadorEventos
{
    [DeclareEventHandler("onActionStart.String.XPrjActionProjectClose")]
    public void AlCerrarProyecto()
    {
        MessageBox.Show("Estás cerrando el proyecto. ¡No olvides guardar tus cambios!");
    }
}