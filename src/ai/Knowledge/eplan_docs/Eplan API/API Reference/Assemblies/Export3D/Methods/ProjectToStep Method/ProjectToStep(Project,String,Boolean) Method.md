# ProjectToStep(Project,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~ProjectToStep(Project,String,Boolean).html

---

Exports project into files in STEP format.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ProjectToStep( 

   Project oProject,

   string strTargetDirectory,

   bool bEachTopLevelParentInSeparateFile

)
```
```

```
```
public:

bool ProjectToStep( 

   Project^ oProject,

   String^ strTargetDirectory,

   bool bEachTopLevelParentInSeparateFile

)
```
```

#### Parameters

*oProject*
:   Project to be exported. Can not be `null`.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

*bEachTopLevelParentInSeparateFile*
:   If `true` then each first level child will be exported in separete file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |

Remarks

If `bEachTopLevelParentInSeparateFile` is `false` then names of files are generated from properties [Eplan.EplApi.DataModel.E3D.InstallationSpacePropertyList.INSTALLATIONSPACE\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpacePropertyList~INSTALLATIONSPACE_FULLNAME.html). If `true` then property [Eplan.EplApi.DataModel.FunctionBasePropertyList.FUNC\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~FUNC_FULLNAME.html) is added at the end of file name.
