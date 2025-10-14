# ReadSettings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~ReadSettings.html

---

Reads settings from settings file.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ReadSettings( 
   string strFilename
)
```
```

```
```
public:
void ReadSettings( 
   String^ strFilename
)
```
```

#### Parameters

*strFilename*
:   Settings file name

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strFilename` is `null`. |
| [System.ArgumentException](#) | Thrown when `strFilename` is empty. |
| [System.ArgumentException](#) | Thrown when file `strFilename` does not exist. |



See Also

#### Reference

[ProjectSettings Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings.html)
  
[ProjectSettings Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings_members.html)