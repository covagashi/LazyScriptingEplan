# DeleteSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~DeleteSetting.html

---

Resets an individual setting to the value of the corresponding default setting. If it has no default setting, the setting is deleted.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void DeleteSetting( 
   string strSetting
)
```
```

```
```
public:
void DeleteSetting( 
   String^ strSetting
)
```
```

#### Parameters

*strSetting*
:   Indicates the path of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be reset or deleted. |



See Also

#### Reference

[Settings Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html)
  
[Settings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings_members.html)