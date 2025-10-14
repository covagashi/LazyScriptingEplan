# Overview

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData_namespace.html

---

This sub-namespace of the electrotechnical data model, contains all classes for accessing master data stored in the project. The classes SymbolLibrary, Symbol, etc. access the symbols included in the project. The class FunctionDefinitionLibrary lists the available function definitions, which can be assigned to a Function object. The macro classes, like WindowMacro provide the possibility to get information from macro files before inserting them into the project.

Classes

|  | Class | Description |
| --- | --- | --- |
| Class | [FunctionDefinitionEnumerator](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionEnumerator.html) | Supports enumeration of function definitions in function definition library. |
| Class | [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) | This class is a interface to function definition library of project. |
| Class | [FunctionDefinitionLibraryPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList.html) | This class represents collection of properties of [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) class. Please check also base classes for other properties which are available for [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) |
| Class | [Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html) | This is a base class for: [PageMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro.html), [WindowMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro.html), [SymbolMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolMacro.html). Class provides basic functionality for macros. This type can be used in order to declare a variable or parameter that holds any type of macro. |
| Class | [PageMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro.html) | This class represents a page macro. |
| Class | [PageMacro.Enums](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro+Enums.html) | This class is used only as container for enumerations, like a name space. |
| Class | [PlotFrame](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame.html) | TODO |
| Class | [PlotFramePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList.html) | This class represents collection of properties of [PlotFrame](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame.html) class. Please check also base classes for other properties which are available for [PlotFrame](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame.html) objects: [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) |
| Class | [PrePlanningMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PrePlanningMacro.html) | TODO |
| Class | [Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html) | This class represents a symbol from a symbol library of a given project. |
| Class | [SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html) | This class is a interface to symbols library of project. |
| Class | [SymbolLibraryPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html) | This class represents collection of properties of [SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html) class. Please check also base classes for other properties which are available for [SymbolLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) |
| Class | [SymbolMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolMacro.html) | This class represents a symbol macro |
| Class | [SymbolPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList.html) | This class represents collection of properties of [Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html) class. Please check also base classes for other properties which are available for [Symbol](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) |
| Class | [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) | This class represents a symbol from a symbol library of a given project. |
| Class | [SymbolVariantPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariantPropertyList.html) | This class represents collection of properties of [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) class. Please check also base classes for other properties which are available for [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) objects: [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) |
| Class | [TransientLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.TransientLayer.html) | The class represents transient layer. |
| Class | [TransientLayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.TransientLayerTable.html) | The class represents table of transient layers. |
| Class | [WindowMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro.html) | This class represents a window macro |
| Class | [WindowMacro.Enums](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro+Enums.html) | This class is used only as container for enumerations, like a name space. |

Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Enumeration | [PageMacro.Enums.NumerationMode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro+Enums+NumerationMode.html) | This enumeration specifies insertion mode, when inserting a macro via the Eplan.EplApi.HeServices.Insert class |
| Enumeration | [Symbol.SymbolType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol+SymbolType.html) |  |
| Enumeration | [TransientLayer.AlignmentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.TransientLayer+AlignmentType.html) | Alignment |
| Enumeration | [WindowMacro.Enums.NumerationMode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro+Enums+NumerationMode.html) | This enumeration specifies insertion mode, when inserting a macro via the Eplan.EplApi.HeServices.Insert class |
| Enumeration | [WindowMacro.Enums.RepresentationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro+Enums+RepresentationType.html) | This enumeration specifies the representation types, which a macro can contain |

See Also

#### Reference

[Eplan.EplApi.DataModelu Assembly](Eplan.EplApi.DataModelu.html)