# Pages(String,PrinterSettings,String,StringCollection,Int32,Boolean,Boolean,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1418.html

---

Prints pages on the specified printer.

Syntax

**C#**
**C++/CLI**


public void Pages( 

   string strPrinterName,

   PrinterSettings pSettings,

   string strFullLinkFileName,

   StringCollection colPages,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   string strTargetFile

)

public:

void Pages( 

   String^ strPrinterName,

   PrinterSettings^ pSettings,

   String^ strFullLinkFileName,

   StringCollection^ colPages,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   String^ strTargetFile

)


#### Parameters

*strPrinterName*
:   Printer name.

*pSettings*
:   [System.Drawing.Printing.PrinterSettings](#) object to specify further printer settings.

*strFullLinkFileName*
:   Full link file name of the project to be printed.

*colPages*
:   Container of pages to be printed. Pages are specified by the full page name.

*dNumber*
:   Number of copies to print.

*bPrintCollate*
:   Collate output.

*bPrintReverse*
:   Reverse printing.

*strTargetFile*
:   Full file name of the output \file in case of printing to \file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \parameters, e.g. the project does not exist. |
| **ArgumentNullException** | Thrown if a parameter is set to null. |
| **ApplicationException** | The \internal interface necessary for printing could not be created. |
| **Eplan\:\:EplApi\:\:Base\:\:BaseException** | An error occurred during the print process. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:PrinterMissing** | The given printer could not be found. |
| **Eplan\:\:EplApi\:\:DataModel\:\:OperationCanceledException** | The print process was canceled by the user. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:UnknownPrinter** | Some undefined error occurred, e.g., HDC could not be created. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the printing process and will be closed subsequently. All pages in `colPages` need to belong to the specified project. Warning! Please check settings under "Workstation->Graphical editing->Print" because they overwrite parameters of the method.
