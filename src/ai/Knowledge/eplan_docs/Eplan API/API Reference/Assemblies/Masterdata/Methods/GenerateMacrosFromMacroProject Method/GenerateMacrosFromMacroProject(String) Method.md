# GenerateMacrosFromMacroProject(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~GenerateMacrosFromMacroProject(String).html

---

Generate macros from project. Project must have property "Type of project" set to "Macro project".

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void GenerateMacrosFromMacroProject( 

   string strFullLinkFileName

)
```
```

```
```
public:

void GenerateMacrosFromMacroProject( 

   String^ strFullLinkFileName

)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project from which the macros will be generated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | A parameter was set to a null reference. |
| **ArgumentException** | Parameters are invalid, e.g. given project name doesn't exist. |
| **ApplicationException** | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be exported. |
