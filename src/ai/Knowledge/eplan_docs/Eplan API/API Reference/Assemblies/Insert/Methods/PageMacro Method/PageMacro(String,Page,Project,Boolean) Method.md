# PageMacro(String,Page,Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PageMacro(String,Page,Project,Boolean).html

---

Inserts a page macro into a project. You need to set the page, after which the new pages are inserted. You can either overwrite already existing pages having the same name, or the macro pages will be appended after the highest existing number of the location.

Syntax

**C#**
**C++/CLI**


public StorableObject[] PageMacro( 

   string strEMPFileName,

   Page oInsertAfterPage,

   Project oProject,

   bool overwrite

)

public:

array<StorableObject^>^ PageMacro( 

   String^ strEMPFileName,

   Page^ oInsertAfterPage,

   Project^ oProject,

   bool overwrite

)


#### Parameters

*strEMPFileName*
:   Full file name of the PageMacro to be inserted.

*oInsertAfterPage*
:   Page after which the macro will be inserted.

*oProject*
:   Project into which the macro will be inserted.

*overwrite*
:   Pages with the same designation will be overwritten..

#### Return Value

Inserted pages and functions which were not placed (with null .Page property)

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
