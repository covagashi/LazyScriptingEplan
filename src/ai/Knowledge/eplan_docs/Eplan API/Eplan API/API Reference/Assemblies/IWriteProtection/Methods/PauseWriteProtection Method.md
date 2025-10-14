# PauseWriteProtection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~PauseWriteProtection.html

---

Temporarily disables write protection. Note that current write protection flags are not cleared.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void PauseWriteProtection( 
   bool bPause
)
```
```

```
```
void PauseWriteProtection( 
   bool bPause
)
```
```

#### Parameters

*bPause*

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionNotSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionNotSet.html) | Thrown if an object has no write protection. |



See Also

#### Reference

[IWriteProtection Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection.html)
  
[IWriteProtection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection_members.html)