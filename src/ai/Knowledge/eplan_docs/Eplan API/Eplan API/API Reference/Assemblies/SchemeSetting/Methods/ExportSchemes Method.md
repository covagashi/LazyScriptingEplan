# ExportSchemes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ExportSchemes.html

---

Export all schemes to file.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ExportSchemes( 
   string strFileName
)
```
```

```
```
public:
void ExportSchemes( 
   String^ strFileName
)
```
```

#### Parameters

*strFileName*
:   The file to export to. Must include the complete path. The file is cleared before.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme. |



See Also

#### Reference

[SchemeSetting Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)
  
[SchemeSetting Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html)