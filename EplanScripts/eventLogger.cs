using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;

public class EventLogger
{
    private const string LOG_FILE_PATH = @"C:\temp\Agent\EplanLog\Events.csv";
    private static bool isLogging = false;
    private static int _lastBookmarkId;
    private static HashSet<string> _processedMessages = new HashSet<string>();

    static EventLogger()
    {
        _lastBookmarkId = new BaseException().GetBookmarkID();
    }

    [DeclareEventHandler("onActionEnd.String.*")]
    public long MyEventHandlerFunction(IEventParameter iEventParameter)
    {
        if (isLogging) return 0;
        isLogging = true;

        try
        {
            string userName = PathMap.SubstitutePath("$(ENVVAR_USERNAME)");
            string projectName = PathMap.SubstitutePath("$(PROJECTNAME)");

            MonitorSystemMessages(userName, projectName);
        }
        catch (Exception exc)
        {
            LogEvent("Error", exc.Message, "", "", "Error");
        }
        finally
        {
            isLogging = false;
        }

        return 0;
    }

    private void MonitorSystemMessages(string userName, string projectName)
    {
        try
        {
            // Obtener bookmark actual para capturar nuevos mensajes
            long currentBookmark = new BaseException().GetBookmarkID();
            
            SysMessagesCollection colSysMsg = new SysMessagesCollection(_lastBookmarkId, MessageLevel.Trace);
            if (colSysMsg.Count > 0)
            {
                SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();

                if (itSysMsg.MoveNext())
                {
                    do
                    {
                        BaseException message = itSysMsg.Current as BaseException;
                        if (message != null)
                        {
                            int level = (int)message.MessageLevel;
                            if (level == 1 || level == 2 || level == 4 || level == 5)
                            {
                                string messageText = message.GetMessageText();
                                string messageId = message.MessageLevel.ToString() + "_" + messageText;

                                if (!_processedMessages.Contains(messageId))
                                {
                                    LogEvent("SystemMessage", messageText, userName, projectName, message.MessageLevel.ToString());
                                    _processedMessages.Add(messageId);
                                }
                            }
                        }
                    } while (itSysMsg.MoveNext());
                    
                    // Actualizar bookmark para próxima iteración
                    _lastBookmarkId = colSysMsg.BookmarkIDEnd;
                }
            }
        }
        catch (Exception ex)
        {
            LogEvent("MonitorError", ex.Message, userName, projectName, "Error");
        }
    }

    private void LogEvent(string eventType, string message, string userName, string projectName, string level)
    {
        try
        {
            Directory.CreateDirectory(Path.GetDirectoryName(LOG_FILE_PATH));

            if (!File.Exists(LOG_FILE_PATH))
            {
            string header = "Fecha,Hora,TipoEvento,Mensaje,Usuario,Proyecto,Nivel\n";
                byte[] headerData = Encoding.UTF8.GetBytes(header);
                using (FileStream fs = new FileStream(LOG_FILE_PATH, FileMode.Create, FileAccess.Write, FileShare.Read))
                {
                    fs.Write(headerData, 0, headerData.Length);
                }
            }

            string logEntry = string.Format("{0},{1},{2},{3},{4},{5},{6}\n",
                DateTime.Now.ToString("yyyy-MM-dd"),
                DateTime.Now.ToString("HH:mm:ss.fff"),
                EscapeCSV(eventType),
                EscapeCSV(message),
                EscapeCSV(userName),
                EscapeCSV(projectName),
                EscapeCSV(level));

            byte[] data = Encoding.UTF8.GetBytes(logEntry);

            using (FileStream fs = new FileStream(LOG_FILE_PATH, FileMode.Append, FileAccess.Write, FileShare.Read))
            {
                fs.Write(data, 0, data.Length);
                fs.Flush();
            }
        }
        catch (Exception exc)
        {
            // Último recurso para errores críticos
            File.AppendAllText(@"C:\temp\Agent\EplanLog\CriticalErrors.txt", 
                DateTime.Now + ": " + exc.Message + "\n");
        }
    }

    private string EscapeCSV(string field)
    {
        if (string.IsNullOrEmpty(field)) return "";
        
        if (field.Contains(",") || field.Contains("\"") || field.Contains("\n"))
        {
            return "\"" + field.Replace("\"", "\"\"") + "\"";
        }
        return field;
    }
}