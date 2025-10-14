# AddDoubleDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddDoubleDefault.html

---

Defines a new setting for a double default.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void AddDoubleDefault( 
   string strSettingPath,
   double[] arrDefaults,
   Range[] arrRange,
   ISettings.CreationFlag eFlag
)
```
```

```
```
public:
void AddDoubleDefault( 
   String^ strSettingPath,
   array<double>^ arrDefaults,
   array<Range^>^ arrRange,
   ISettings.CreationFlag eFlag
)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*arrDefaults*
:   Array of default values

*arrRange*
:   Array of [Range](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Range.html). Used for value validation.

*eFlag*
:   [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values. Warning: double values are stored with precision to 15 digits only!



See Also

#### Reference

[Settings Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html)
  
[Settings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings_members.html)