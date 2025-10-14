# GetTypeOfSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~GetTypeOfSetting.html

---

Returns the type of the setting.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
ISettings.SettingType GetTypeOfSetting( 
   string strSettingPath
)
```
```

```
```
ISettings.SettingType GetTypeOfSetting( 
   String^ strSettingPath
)
```
```

#### Parameters

*strSettingPath*
:   path to settings

#### Return Value

the type of the setting as enum

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |



See Also

#### Reference

[ISettings Interface](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings.html)
  
[ISettings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings_members.html)