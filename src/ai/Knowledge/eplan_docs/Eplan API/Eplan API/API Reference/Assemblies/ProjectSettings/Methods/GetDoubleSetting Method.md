# GetDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetDoubleSetting.html

---

Reads double value from project settings

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual double GetDoubleSetting( 
   string strSettingPath,
   int nIdx
)
```
```

```
```
public:
virtual double GetDoubleSetting( 
   String^ strSettingPath,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   Path to settings

*nIdx*
:   0\-based index.

#### Return Value

Value read from project settings

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from project settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [System.ArgumentException](#) | Thrown when setting path doesn't exist. |

Remarks

Warning: double values are stored with precision to 15 digits only!



See Also

#### Reference

[ProjectSettings Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings.html)
  
[ProjectSettings Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings_members.html)