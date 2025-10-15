# AddMultiLangStringDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddMultiLangStringDefault.html

---

Defines a new setting for a multilanguage string default.

Syntax

**C#**
**C++/CLI**


public void AddMultiLangStringDefault( 

   string strSettingPath,

   MultiLangString[] arrDefaults,

   MultiLangString[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddMultiLangStringDefault( 

   String^ strSettingPath,

   array<MultiLangString^>^ arrDefaults,

   array<MultiLangString^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting

*arrDefaults*
:   Array of default values

*arrRange*
:   Ranges used for value validation

*eFlag*
:   [Eplan.EplApi.Base.ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
