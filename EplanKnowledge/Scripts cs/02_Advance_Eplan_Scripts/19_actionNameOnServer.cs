using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;

public class EventLogger
{
    private static readonly HttpClient client = new HttpClient();
    private const string SERVER_URL = "http://localhost:8000"; // Ajusta esta URL según tu configuración

    [DeclareEventHandler("onActionEnd.String.*")]
    public long MyEventHandlerFunction(IEventParameter iEventParameter)
    {
        try
        {
            EventParameterString oEventParameterString = new EventParameterString(iEventParameter);
            string strActionName = oEventParameterString.String;

            // Enviar el evento al servidor
            SendEventToServer(strActionName); 
        }
        catch (Exception ex)
        {
            System.Windows.Forms.MessageBox.Show(string.Format("Error: {0}", ex.Message), "MyEventHandler");
        }

        return 0;
    }

    private async Task SendEventToServer(string actionName)
    {
        try
        {
            string json = string.Format("{{\"event\":\"onActionEnd.String.{0}\",\"timestamp\":\"{1}\"}}", actionName, DateTime.Now);
            var content = new StringContent(json, Encoding.UTF8, "application/json");

            HttpResponseMessage response = await client.PostAsync(SERVER_URL, content);
            string responseContent = await response.Content.ReadAsStringAsync();

            if (!response.IsSuccessStatusCode)
            {
                throw new Exception(string.Format("Server error: {0}. Message: {1}", response.StatusCode, responseContent));
            }
            
        }
        catch (Exception ex)
        {
            System.Diagnostics.Trace.WriteLine(string.Format("Error sending event to server: {0}", ex.Message));
            
        }
    }
}