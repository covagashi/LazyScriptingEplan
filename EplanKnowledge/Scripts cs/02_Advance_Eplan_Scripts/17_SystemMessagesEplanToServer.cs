using System;
using System.Net.Http;
using System.Text;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;

public class SystemMessageLogger
{
    private static readonly HttpClient client = new HttpClient();
    private const string SERVER_URL = "http://localhost:8000/log";
    private const string LOG_FILE_PATH = @"C:\Temp\EplanErrorLog.txt";
    private static int lastBookmarkID = 0;

    [DeclareEventHandler("onActionEnd.String.*")]
    public void MyEventHandlerFunction(IEventParameter iEventParameter)
    {
        try
        {
            SysMessagesCollection colSysMsg = new SysMessagesCollection(lastBookmarkID, MessageLevel.Error);
        
            if (colSysMsg.Count > 0)
            {
                BaseException lastMessage = colSysMsg.Cast<BaseException>().LastOrDefault();
            
                if (lastMessage != null)
                {
                    string message = "Error: " + lastMessage.ToString();
                    SendMessageToServer(message).Wait();
                    WriteTestFile(message);
                }
            
                lastBookmarkID = colSysMsg.BookmarkIDEnd;
            }
        }
        catch (Exception ex)
        {
            WriteTestFile("Error in MyEventHandlerFunction: " + ex.ToString());
        }
    }

    private async Task SendMessageToServer(string message)
    {
        try
        {
            var content = new StringContent(message, Encoding.UTF8, "text/plain");
            HttpResponseMessage response = await client.PostAsync(SERVER_URL, content);
            
            if (response.IsSuccessStatusCode)
            {
                WriteTestFile("Message ok: " + message);
            }
            else
            {
                WriteTestFile("Error sending message to server. Código: " + response.StatusCode);
            }
        }
        catch (Exception ex)
        {
            WriteTestFile("Exception when sending message to server: " + ex.ToString());
        }
    }

    private void WriteTestFile(string message)
    {
        try
        {
            using (StreamWriter sw = File.AppendText(LOG_FILE_PATH))
            {
                sw.WriteLine(DateTime.Now + ": " + message);
            }
        }
        catch (Exception ex)
        {            
            Console.WriteLine("Error writing to file: " + ex.Message);
        }
    }
}