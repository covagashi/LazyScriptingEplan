# GetListOfAllSettings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetListOfAllSettings.html

---

Determines all settings.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void GetListOfAllSettings( 
   ref StringCollection colOfSettings,
   bool bAbsolutPath
)
```
```

```
```
public:
virtual void GetListOfAllSettings( 
   StringCollection^% colOfSettings,
   bool bAbsolutPath
)
```
```

#### Parameters

*colOfSettings*
:   Container to which existing settings are output.

*bAbsolutPath*
:   Controls the output:

    True: Path of settings is absolute.

    False: Relative paths of settings are output.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |



See Also

#### Reference

[SettingNode Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html)
  
[SettingNode Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode_members.html)