# GetStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetStringSetting.html

---

Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string GetStringSetting( 
   string strSettingPath,
   int nIdx
)
```
```

```
```
public:
String^ GetStringSetting( 
   String^ strSettingPath,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

*nIdx*
:   Indicates the index.

#### Return Value

Returns the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |



See Also

#### Reference

[SchemeSetting Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)
  
[SchemeSetting Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html)