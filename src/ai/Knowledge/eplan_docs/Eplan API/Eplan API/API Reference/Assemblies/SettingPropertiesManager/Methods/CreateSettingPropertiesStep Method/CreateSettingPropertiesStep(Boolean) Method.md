# CreateSettingPropertiesStep(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesManager~CreateSettingPropertiesStep(Boolean).html

---

Creates object representing a setting properties step.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public SettingPropertiesStep CreateSettingPropertiesStep( 
   bool bCreateTransaction
)
```
```

```
```
public:
SettingPropertiesStep^ CreateSettingPropertiesStep( 
   bool bCreateTransaction
)
```
```

#### Parameters

*bCreateTransaction*
:   If `true` then read-write transaction is created.

#### Return Value

New [SettingPropertiesStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesStep.html) object.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SettingStepAlreadyOpenException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingStepAlreadyOpenException.html) | Thrown when a [SettingPropertiesStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesStep.html) is already created and used. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if `bCreateTransaction` and when a Transaction object has already been obtained and not disposed. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown if `bCreateTransaction` and when a read-write transaction is being opened while read-only transaction is running or when a read-only transaction is being opened while read-write transaction is running. |

Remarks

If a transaction is created, it is automatically committed when setting properties step object is being disposed.



See Also

#### Reference

[SettingPropertiesManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesManager.html)
  
[SettingPropertiesManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesManager_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Helpers.SettingPropertiesManager~CreateSettingPropertiesStep.html)