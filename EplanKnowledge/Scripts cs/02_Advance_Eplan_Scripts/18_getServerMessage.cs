using System;
using System.Net.Http;
using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;

public class ConexionServidor
{
    [Start]
    public void Execute()
    {
        ObtenerMensajeDelServidor();
    }

    private void ObtenerMensajeDelServidor()
    {
        using (var client = new HttpClient())
        {
            try
            {
                string url = "http://localhost:8000";
                HttpResponseMessage response = client.GetAsync(url).Result;
                
                if (response.IsSuccessStatusCode)
                {
                    string contenido = response.Content.ReadAsStringAsync().Result;
                    MessageBox.Show("Mensaje del servidor: " + contenido);
                }
                else
                {
                    MessageBox.Show("Error: " + response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error en la petición: " + ex.Message);
            }
        }
    }
}