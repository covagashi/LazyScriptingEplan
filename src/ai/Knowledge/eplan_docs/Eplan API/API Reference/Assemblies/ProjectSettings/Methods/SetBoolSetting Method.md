# SetBoolSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetBoolSetting.html

---

Sets the value of a project setting in a specified path.

Syntax

**C#**
**C++/CLI**


public virtual void SetBoolSetting( 

   string strSettingPath,

   bool bValue,

   int nIdx

)

public:

virtual void SetBoolSetting( 

   String^ strSettingPath,

   bool bValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Path to the project setting

*bValue*
:   Value to be set

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the `strSettingsPath` parameter is `NULL`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the value cannot be set. |
| [System.ArgumentException](#) | Thrown if the settings path doesn't exist. |
