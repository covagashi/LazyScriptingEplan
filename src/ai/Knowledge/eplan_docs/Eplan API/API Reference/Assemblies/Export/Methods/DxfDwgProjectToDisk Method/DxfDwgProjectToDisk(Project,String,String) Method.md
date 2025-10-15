# DxfDwgProjectToDisk(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgProjectToDisk(Project,String,String).html

---

Exports a complete project as DXF/DWG files. Export settings are taken from the scheme passed in the 'sScheme' parameter

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void DxfDwgProjectToDisk( 

   Project prj,

   string sScheme,

   string sTargetDir

)
```
```

```
```
public:

void DxfDwgProjectToDisk( 

   Project^ prj,

   String^ sScheme,

   String^ sTargetDir

)
```
```

#### Parameters

*prj*
:   Project to be exported.

*sScheme*
:   A settings scheme to use.

*sTargetDir*
:   The output directory.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, for \example a wrong scheme. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for exporting could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

This method uses a scheme from "USER.DXF.SCHEMES". All necessary settings are set in this scheme. If you pass an empty string to "sScheme", the last used scheme will be used which is currently set in GUI. If no scheme does exist with the given scheme name, a BaseException will be thrown. Depending on the scheme settings, exported pages' names can be prefixed to create a folder-like structure. Options available in the scheme for sub-folder generation are: none, from page tree, from page properties.
