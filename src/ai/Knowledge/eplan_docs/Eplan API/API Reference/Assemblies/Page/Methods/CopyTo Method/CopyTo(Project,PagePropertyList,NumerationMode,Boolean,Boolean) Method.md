# CopyTo(Project,PagePropertyList,NumerationMode,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~CopyTo(Project,PagePropertyList,NumerationMode,Boolean,Boolean).html

---

Creates copy of this page.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Page CopyTo( 

   Project pProject,

   PagePropertyList pPageName,

   PageMacro.Enums.NumerationMode nNumerationMode,

   bool bOverwrite,

   bool bDontUseProgressBar

)
```
```

```
```
public:

Page^ CopyTo( 

   Project^ pProject,

   PagePropertyList^ pPageName,

   PageMacro.Enums.NumerationMode nNumerationMode,

   bool bOverwrite,

   bool bDontUseProgressBar

)
```
```

#### Parameters

*pProject*
:   Target project in which copy of page will be created. Can be `null` or invalid.

*pPageName*
:   List of property defining name of new page. Can't be `null`.

*nNumerationMode*
:   Determines how devices located on page will be renumbered.

*bOverwrite*
:   Controls if new page will overwrite existing page.

*bDontUseProgressBar*
:   If set to true no ProgressBar will be shown.

#### Return Value

Returns newly created page or `null` if page of same name existed and was not overwritten.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when required argument is `null`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal problem has occurred during coping the page. Please check exception message for more info. |

Remarks

Page is copied and inserted into target project with copy of all placement located on this page. New page gets name specified in parameter `pPageName`. Function can be forced to overwrite a page if one with the same name will already exists in target project if value of `bOverwrite` will be true. If in such situation `bOverwrite` will be false then the function will not report an error but will return `null`.
