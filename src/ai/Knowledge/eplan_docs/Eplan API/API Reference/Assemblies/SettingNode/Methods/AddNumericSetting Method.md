# AddNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddNumericSetting.html

---

Defines a new setting for a numeric value.

Syntax

**C#**
**C++/CLI**


public void AddNumericSetting( 

   string strSettingPath,

   int[] arrValues,

   Range[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddNumericSetting( 

   String^ strSettingPath,

   array<int>^ arrValues,

   array<Range^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*arrValues*
:   Array of values added to the setting

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

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
