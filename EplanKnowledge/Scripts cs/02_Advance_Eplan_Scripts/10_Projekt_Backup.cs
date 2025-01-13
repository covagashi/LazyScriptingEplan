using System;
using System.Windows.Forms;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;

public class Class
{
    [Start]
    public void Function()
    {
        string strProjectpath =
            PathMap.SubstitutePath("$(PROJECTPATH)");
        string strProjectname = PathMap.SubstitutePath("$(PROJECTNAME)");
        string strFullProjectname = PathMap.SubstitutePath("$(P)");

        string strDate = DateTime.Now.ToString("yyyy-MM-dd");
        string strTime = DateTime.Now.ToString("hh-mm-ss");
        string strBackupDirectory = strProjectpath + @"\Backup\";
        string strBackupFilename = strProjectname + "_Backup_"
            + strDate + "_" + strTime;

        if (!System.IO.Directory.Exists(strBackupDirectory))
        {
            System.IO.Directory.CreateDirectory(strBackupDirectory);
        }

        Progress oProgress = new Progress("SimpleProgress");
        oProgress.SetAllowCancel(true);
        oProgress.SetAskOnCancel(true);
        oProgress.BeginPart(100, "");
        oProgress.SetTitle("Backup");
        oProgress.ShowImmediately();

        if (!oProgress.Canceled())
        {
            CommandLineInterpreter oCLI = new CommandLineInterpreter();
            ActionCallingContext acc = new ActionCallingContext();

            acc.AddParameter("BACKUPMEDIA", "DISK");
            acc.AddParameter("ARCHIVENAME", strBackupFilename);
            acc.AddParameter("BACKUPMETHOD", "BACKUP");
            acc.AddParameter("COMPRESSPRJ", "1");
            acc.AddParameter("INCLEXTDOCS", "1");
            acc.AddParameter("BACKUPAMOUNT", "BACKUPAMOUNT_ALL");
            acc.AddParameter("INCLIMAGES", "1");
            acc.AddParameter("LogMsgActionDone", "true");
            acc.AddParameter("DESTINATIONPATH", strBackupDirectory);
            acc.AddParameter("PROJECTNAME", strFullProjectname);
            acc.AddParameter("TYPE", "PROJECT");

            oCLI.Execute("backup", acc);
        }

        oProgress.EndPart(true);

        MessageBox.Show(
            "Backup wurde erfolgreich erstellt:\n"
            + strBackupFilename,
            "Hinweis",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information
            );

        return;

    }
}