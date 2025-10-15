# AddMultiLangStringDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddMultiLangStringDefault.html

---

Defines a new default setting for a multilanguage string value.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void AddMultiLangStringDefault( 

   string strSettingPath,

   MultiLangString[] arrDefaults,

   MultiLangString[] arrRange,

   ISettings.CreationFlag eFlag

)
```
```

```
```
public:

void AddMultiLangStringDefault( 

   String^ strSettingPath,

   array<MultiLangString^>^ arrDefaults,

   array<MultiLangString^>^ arrRange,

   ISettings.CreationFlag eFlag

)
```
```

#### Parameters

*strSettingPath*
:   Indicates the path of the setting

*arrDefaults*
:   Array of defaults added to the setting

*arrRange*
:   Ranges used for value validation

*eFlag*
:   [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
