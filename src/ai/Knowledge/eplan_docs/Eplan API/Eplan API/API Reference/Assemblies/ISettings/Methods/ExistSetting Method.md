# ExistSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~ExistSetting.html

---

Check if there exist a setting on path given as a parameter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
bool ExistSetting( 
   string strSettingPath
)
```
```

```
```
bool ExistSetting( 
   String^ strSettingPath
)
```
```

#### Parameters

*strSettingPath*
:   path to settings

#### Return Value

bool indicating if the setting exist

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |



See Also

#### Reference

[ISettings Interface](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings.html)
  
[ISettings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings_members.html)