# GetNumericDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetNumericDefault.html

---

Returns default numeric value of a setting. The index starts at 0.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int GetNumericDefault( 
   string strSettingPath,
   int nIdx
)
```
```

```
```
public:
int GetNumericDefault( 
   String^ strSettingPath,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Default numeric value

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |



See Also

#### Reference

[Settings Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html)
  
[Settings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings_members.html)