# IXMLProcessor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor.html

---

Interface for implementing an XML processor.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public interface IXMLProcessor : IInterface
```
```

```
```
public interface class IXMLProcessor : public IInterface
```
```





Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [InterfaceName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface~InterfaceName.html) | This name is used to register the type as an interface. (Inherited from [Eplan.EplApi.ApplicationFramework.IInterface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [CanExport](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~CanExport.html) | Indicates whether the converter provides an export option. |
| Method | [CanImport](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~CanImport.html) | Indicates whether the converter can convert external formats to XML. |
| Method | [Export](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~Export.html) | Converts the XML file to a special file. |
| Method | [GetErrorMessage](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~GetErrorMessage.html) | Returns an error message if an error occured during export/import. |
| Method | [GetFileFilter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~GetFileFilter.html) | Returns the filter string for the file selection box. |
| Method | [GetName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~GetName.html) | Returns the name of the converter. |
| Method | [GetOption](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~GetOption.html) | Returns a settings dialog for this processor. Dialog is only created, but not displayed! |
| Method | [Import](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~Import.html) | Conversion from sImportFile to sXmlFile. sXmlFile might be passed as "". In this case, the converter must set a file name. EContext may point to an EProgress object to support a progress bar. Returns true if successful. |
| Method | [PostExport](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~PostExport.html) | Is called after export has been completed. |
| Method | [PostImport](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~PostImport.html) | Is called after import has been completed. |

[Top](#top)
