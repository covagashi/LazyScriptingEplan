# ProjectToJT(Project,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~ProjectToJT(Project,String,String).html

---

Exports project into files in JT format.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ProjectToJT( 

   Project oProject,

   string strTargetDirectory,

   string strScheme

)
```
```

```
```
public:

bool ProjectToJT( 

   Project^ oProject,

   String^ strTargetDirectory,

   String^ strScheme

)
```
```

#### Parameters

*oProject*
:   Project to be exported. Can not be `null`.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

*strScheme*
:   Scheme used for export.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
