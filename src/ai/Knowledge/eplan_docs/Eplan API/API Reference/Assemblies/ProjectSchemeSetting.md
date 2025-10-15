# ProjectSchemeSetting

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting.html

---

Class for editing settings that are grouped into project schemes

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)  
      **Eplan.EplApi.DataModel.ProjectSchemeSetting**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class ProjectSchemeSetting : Eplan.EplApi.Base.SchemeSetting
```
```

```
```
public ref class ProjectSchemeSetting : public Eplan.EplApi.Base.SchemeSetting
```
```

Example

Example of using ProjectSchemeSetting class

- [C#](#i-tab-content-9bc636cf-f381-402d-a09c-202d8947762f)

```
ProjectSchemeSetting oProjectSchemeSetting = new ProjectSchemeSetting();

oProjectSchemeSetting.Init("XEsInspectionGui.Scheme_Verifications", m_oTestProject);



string strSchemeName = "Offline";

if(oProjectSchemeSetting.CheckIfSchemeExists(strSchemeName))

{

    oProjectSchemeSetting.SetScheme(strSchemeName);

    oProjectSchemeSetting.SetNumericSetting("001001.VerificationType", 1, 0);

}



```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectSchemeSetting Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~_ctor().html) | Default constructor |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Description.html) | Returns a multilingual description text of the scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Property | [MLangName](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~MLangName.html) | Returns a multilingual scheme name. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Property | [ReadOnly](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ReadOnly.html) | Gives write permission to settings of this scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CheckIfSchemeExists](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CheckIfSchemeExists.html) | Checks whether a scheme is defined. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [CopyScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CopyScheme.html) | Copy an existing scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [CountSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CountSetting.html) | Number of additional settings existing under the specified setting name. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [CreateScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CreateScheme.html) | Create a new scheme with a specified name, description and the node name for the settings. The data for the new scheme is specified by P8 for each scheme type. The data is the same as the new button in the scheme dialog of P8. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [Dispose()](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Dispose().html) | Virtual deterministic destructor. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [ExportScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ExportScheme.html) | Export a scheme to file. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [ExportSchemes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ExportSchemes.html) | Export all schemes to file. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetBoolSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetCount.html) | Returns the number of various schemes in this scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetDoubleSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetLastUsed](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetLastUsed.html) | Returns the last used scheme name (node LastUsed). (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetLocalizedNameSettingPath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetLocalizedNameSettingPath.html) | Returns Setting path to the localized name of this scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetMultiLangStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetName](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetName.html) | Returns a language-independent, internal scheme identifier. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetNodeHandle](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetNodeHandle.html) | Returns the [Eplan.EplApi.Base.SettingNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html) of the data node of the current setting. The individual settings can now be accessed via the functions of the [Eplan.EplApi.Base.SettingNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html). (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetNumericSetting.html) | Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [GetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [ImportScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportScheme.html) | Import a scheme from file. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [ImportSchemes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportSchemes.html) | Import all schemes from file. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [Init](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init.html) | Overloaded. Overridden. Initializes object with a settings node path. |
| Public Method | [RemoveScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~RemoveScheme.html) | Remove a new scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [ResetScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ResetScheme.html) | Sets LastUsed as the current scheme. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [Set](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Set.html) | Overridden. Setup internal members |
| Public Method | [SetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetBoolSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetDoubleSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetLastUsed](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetLastUsed.html) | Sets the strName scheme as the current one. Value in node LastUsed will be strName (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetMultiLangStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetNumericSetting.html) | Sets the value of settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetScheme.html) | Overloaded. Sets a scheme by its name (LastUsed remains unchanged!) (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |
| Public Method | [SetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. (Inherited from [Eplan.EplApi.Base.SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)) |

[Top](#top)
