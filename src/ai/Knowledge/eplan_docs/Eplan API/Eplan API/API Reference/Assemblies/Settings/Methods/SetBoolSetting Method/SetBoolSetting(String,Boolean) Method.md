# SetBoolSetting(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetBoolSetting(String,Boolean).html

---

Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetBoolSetting( 
   string strSettingPath,
   bool bValue
)
```
```

```
```
public:
void SetBoolSetting( 
   String^ strSettingPath,
   bool bValue
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*bValue*
:   Indicates the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be set. |



See Also

#### Reference

[Settings Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html)
  
[Settings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings_members.html)
  
[Overload List](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetBoolSetting.html)