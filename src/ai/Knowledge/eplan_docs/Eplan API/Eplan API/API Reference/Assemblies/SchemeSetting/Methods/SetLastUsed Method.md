# SetLastUsed Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetLastUsed.html

---

Sets the strName scheme as the current one. Value in node LastUsed will be strName

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetLastUsed( 
   string strName
)
```
```

```
```
public:
void SetLastUsed( 
   String^ strName
)
```
```

#### Parameters

*strName*
:   Name of the scheme to which LastUsed is to be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme. |



See Also

#### Reference

[SchemeSetting Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)
  
[SchemeSetting Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html)