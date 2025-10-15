# PDFComments(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import~PDFComments(Project,String).html

---

Imports comments from PDF file.

Syntax

**C#**
**C++/CLI**


public int PDFComments( 

   Project oProject,

   string strFileName

)

public:

int PDFComments( 

   Project^ oProject,

   String^ strFileName

)


#### Parameters

*oProject*
:   Project to which comments from pdf will be imported. Can't be `null`.

*strFileName*
:   Full file name of the PDF file to be imported. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | API can't get access to this functionality of P8. A reason for this could be the lack of necessary rights or licenses. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please read the exception message. |
