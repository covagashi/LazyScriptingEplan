# ImportData(Project,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.HarnessService~ImportData(Project,String,Boolean).html

---

Imports Harness data from a file.

Syntax

**C#**
**C++/CLI**


public StorableObject[] ImportData( 

   Project oProject,

   string strFileName,

   bool bShowAdjustmentDlg

)

public:

array<StorableObject^>^ ImportData( 

   Project^ oProject,

   String^ strFileName,

   bool bShowAdjustmentDlg

)


#### Parameters

*oProject*
:   Project into which the Harness data will be imported.

*strFileName*
:   Full file name of the file to import.

*bShowAdjustmentDlg*
:   Shows adjustment dialog when true.

#### Return Value

An array of created or modified StorableObjects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for importing Harness data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. |
