# SymbolReferencePropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html

---

This class represents collection of properties of [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) class. Please check also base classes for other properties which are available for [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) objects: [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            **Eplan.EplApi.DataModel.SymbolReferencePropertyList**  
               [Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList.html)  
               [Eplan.EplApi.DataModel.DynamicConnectionLinePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLinePropertyList.html)  
               [Eplan.EplApi.DataModel.FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html)  
               [Eplan.EplApi.DataModel.MacroBoxPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBoxPropertyList.html)  
               [Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList.html)  
               [Eplan.EplApi.DataModel.PotentialDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)  
               [Eplan.EplApi.DataModel.StrandConnectorPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandConnectorPropertyList.html)  
               [Eplan.EplApi.DataModel.StrandInterConnectorPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandInterConnectorPropertyList.html)

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
[DefaultMember("Property")]
public class SymbolReferencePropertyList : PlacementPropertyList
```
```

```
```
[DefaultMember("Property")]
public ref class SymbolReferencePropertyList : public PlacementPropertyList
```
```

Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

- [C#](#i-tab-content-19dc4616-9206-48a3-9b1e-b425547a0bb0)

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
| Public Constructor | [SymbolReferencePropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_SYMB\_DESC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_DESC().html) | Symbol description (function) # 20114. |
| Public Property | [FUNC\_SYMB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NAME().html) | Symbol name # 20112. |
| Public Property | [FUNC\_SYMB\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NUMBER().html) | Symbol number # 20168. |
| Public Property | [FUNC\_SYMB\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_VARIANT().html) | Symbol variant # 20113. |
| Public Property | [FUNC\_SYMBLIB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBLIB_NAME().html) | Symbol library # 20111. |
| Public Property | [FUNC\_SYMBOL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBOL().html) | Symbol # 20575. |
| Public Property | [INSTANCE\_ACTIVE\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_ACTIVE_PROPERTYSET().html) | Property arrangement # 19307. |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_FULLPLACEMENTLOCATION().html) | Placement # 19007. |
| Public Property | [INSTANCE\_PAGEFULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGEFULLNAME().html) | Page name (full) # 19023. |
| Public Property | [INSTANCE\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGENAME().html) | Page name # 19022. |
| Public Property | [INSTANCE\_PAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGETYPE().html) | Page type # 19020. |
| Public Property | [INSTANCE\_PATHID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PATHID().html) | Column number # 19005. |
| Public Property | [INSTANCE\_POSID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_POSID().html) | Row number # 19006. |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_TYPE().html) | Representation type / report type # 19021. |
| Public Property | [INSTANCE\_USER\_DEFINED\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_USER_DEFINED_PROPERTYSET().html) | User-defined property arrangement: Name # 19008. |
| Public Property | [INSTANCE\_XCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_XCOORD().html) | X coordinate # 19002. |
| Public Property | [INSTANCE\_YCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_YCOORD().html) | Y coordinate # 19003. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of SymbolReferencePropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |

[Top](#top)




See Also

#### Reference

[SymbolReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[SymbolReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)
  
[PlacementPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)