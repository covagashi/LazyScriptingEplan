# StorableObjectPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html

---

This class represents collection of properties of [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) class. Please check also base classes for other properties which are available for [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) objects:

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      **Eplan.EplApi.DataModel.StorableObjectPropertyList**  
         [Eplan.EplApi.DataModel.ArticlePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)  
         [Eplan.EplApi.DataModel.ArticleReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)  
         [Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList.html)  
         [Eplan.EplApi.DataModel.ConnectionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)  
         [Eplan.EplApi.DataModel.DeviceListEntryPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList.html)  
         [Eplan.EplApi.DataModel.E3D.Group3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3DPropertyList.html)  
         [Eplan.EplApi.DataModel.E3D.PlaceHolder3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3DPropertyList.html)  
         [Eplan.EplApi.DataModel.E3D.Placement3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)  
         [Eplan.EplApi.DataModel.FunctionDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinitionPropertyList.html)  
         [Eplan.EplApi.DataModel.LocationPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList.html)  
         [Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList.html)  
         [Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html)  
         [Eplan.EplApi.DataModel.MasterData.SymbolPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList.html)  
         [Eplan.EplApi.DataModel.MergedArticleReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)  
         [Eplan.EplApi.DataModel.MergedConnectionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnectionPropertyList.html)  
         [Eplan.EplApi.DataModel.MergedFunctionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunctionPropertyList.html)  
         [Eplan.EplApi.DataModel.OptionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionBasePropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
         [Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)  
         [Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList.html)  
         [Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList.html)  
         [Eplan.EplApi.DataModel.PlcIOPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList.html)  
         [Eplan.EplApi.DataModel.ProjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html)

Syntax

**C#**
**C++/CLI**


[DefaultMember("Property")]

public class StorableObjectPropertyList : UniversalPropertyList

[DefaultMember("Property")]

public ref class StorableObjectPropertyList : public UniversalPropertyList


Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

**C#**

```
// creation of persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// now oFunction.Properties.FUNC_COMMENT is equal "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// now oFunction.Properties.FUNC_COMMENT is equal "Test"

// creation of transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// now oTransientPropertyList.FUNC_COMMENT is equal "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [StorableObjectPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~_ctor.html) | Overloaded. |

[Top](#top)

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Object identification # 2000. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of StorableObjectPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |

[Top](#top)
