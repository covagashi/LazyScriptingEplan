# ProjectSettings

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings.html

---

The classes representing P8 project settings.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.ProjectSettings**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class ProjectSettings : Eplan.EplApi.Base.ISettings
```
```

```
```
public ref class ProjectSettings : public Eplan.EplApi.Base.ISettings
```
```

Remarks

For more details about inherited members see [Eplan.EplApi.Base.ISettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings.html).



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectSettings Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~_ctor.html) | Constructor. |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddBoolDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddBoolDefault.html) | Defines a new setting for a boolean value. |
| Public Method | [AddBoolSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddBoolSetting.html) | Defines a new setting for a boolean value. |
| Public Method | [AddDoubleDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddDoubleDefault.html) | Defines a new setting for a double default. |
| Public Method | [AddDoubleSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddDoubleSetting.html) | Defines a new setting for a double value. |
| Public Method | [AddMultiLangStringDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddMultiLangStringDefault.html) | Defines a new setting for a multilanguage string default. |
| Public Method | [AddMultiLangStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddMultiLangStringSetting.html) | Defines a new setting for a multilanguage string value. |
| Public Method | [AddNumericDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddNumericDefault.html) | Defines a new setting for a numeric default. |
| Public Method | [AddNumericSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddNumericSetting.html) | Defines a new setting for a numeric value. |
| Public Method | [AddStringDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddStringDefault.html) | Defines a new setting for a string default. |
| Public Method | [AddStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddStringSetting.html) | Defines a new setting for a string value. |
| Public Method | [DeleteSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~DeleteSetting.html) | Resets a setting to the value from the default settings. If the setting has no default value, it will be deleted. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~Dispose().html) | Destructor for deterministic finalization of Cable object. |
| Public Method | [ExistSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~ExistSetting.html) | Check if there exist a setting on path given as a parameter. |
| Public Method | [GetBoolSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetBoolSetting.html) | Reads bool value from project settings |
| Public Method | [GetCountOfValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetCountOfValues.html) | Returnes the count of indexed values that are used already by the project setting. |
| Public Method | [GetDoubleSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetDoubleSetting.html) | Reads double value from project settings |
| Public Method | [GetExpandedStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetExpandedStringSetting.html) | Reads value from project settings. Substitutes path fragments (like $Eplan). |
| Public Method | [GetMultiLangStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetMultiLangStringSetting.html) | Reads [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) value from project settings |
| Public Method | [GetNumericSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetNumericSetting.html) | Reads numeric value from project settings. It can be 16 bit or 32 bit, signed or unsigned setting. |
| Public Method | [GetStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetStringSetting.html) | Reads string value from project settings |
| Public Method | [GetTypeOfSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetTypeOfSetting.html) | Returns the type of the setting. |
| Public Method | [ReadSettings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~ReadSettings.html) | Reads settings from settings file. |
| Public Method | [SetBoolSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetBoolSetting.html) | Sets the value of a project setting in a specified path. |
| Public Method | [SetDoubleSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetDoubleSetting.html) | Sets the value of a project setting in a specified path. |
| Public Method | [SetMultiLangStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetMultiLangStringSetting.html) | Sets the value of a project setting in a specified path. |
| Public Method | [SetNumericSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetNumericSetting.html) | Sets the value of a project setting in a specified path. The type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on the setting type. |
| Public Method | [SetStringSetting](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetStringSetting.html) | Overloaded. Sets the value of a project setting in a specified path. |

[Top](#top)
