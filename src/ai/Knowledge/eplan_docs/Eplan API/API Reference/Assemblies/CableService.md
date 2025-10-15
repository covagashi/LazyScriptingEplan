# CableService

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService.html

---

Class providing functionality for cables: numbering, automatic cable selection, generate cable automatically, delete automatically generated cables and add up cable length.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.CableService**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class CableService
```
```

```
```
public ref class CableService
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [CableService Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~_ctor.html) | Default constructor |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AutoCableSelection](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~AutoCableSelection.html) | Overloaded. Commits an automatic cable selection in the project. |
| Public Method | [CreateAutoCable](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~CreateAutoCable.html) | Overloaded. Automatically generate cables in the given project. |
| Public Method | [DeleteAutoCable](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DeleteAutoCable.html) | Overloaded. removes automatically created cables and connection definition points. Automatically set names also will be deleted. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~Dispose().html) | Destructor |
| Public Method | [DoReassignWires](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DoReassignWires.html) | Overloaded. All wires in cable are assigned to a matching template of the cable or shielding. User specifies templates to which wires will be assigned. Works only for [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) or [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) with category **Eplan.EplApi.DataModel.Function.Enums.Category.Shielding**. |
| Public Method | [FindMatchingTemplatePairs](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~FindMatchingTemplatePairs.html) | Matches templates and wires. No changes on objects are performed. |
| Public Method | [RenumberCables](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~RenumberCables.html) | Overloaded. Method for numbering cables in a project. |

[Top](#top)
