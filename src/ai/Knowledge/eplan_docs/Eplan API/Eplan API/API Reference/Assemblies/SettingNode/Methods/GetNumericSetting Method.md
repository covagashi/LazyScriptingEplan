# GetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetNumericSetting.html

---

Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual int GetNumericSetting( 
   string strSettingPath,
   int nIdx
)
```
```

```
```
public:
virtual int GetNumericSetting( 
   String^ strSettingPath,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*nIdx*
:   0-based index.

#### Return Value

value read from settings

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |



See Also

#### Reference

[SettingNode Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html)
  
[SettingNode Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode_members.html)