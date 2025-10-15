# InstallationSpacesToJT(IEnumerable<InstallationSpace>,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1353.html

---

Exports given installation spaces into files in JT format.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool InstallationSpacesToJT( 

   IEnumerable<InstallationSpace> listInstallationSpaces,

   string strTargetDirectory,

   string strScheme

)
```
```

```
```
public:

bool InstallationSpacesToJT( 

   IEnumerable<InstallationSpace^>^ listInstallationSpaces,

   String^ strTargetDirectory,

   String^ strScheme

)
```
```

#### Parameters

*listInstallationSpaces*
:   Collection of installation spaces which will be exported. Can not be `null` or empty.

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
