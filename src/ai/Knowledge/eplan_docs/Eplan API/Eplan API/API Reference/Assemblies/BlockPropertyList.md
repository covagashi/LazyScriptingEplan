# BlockPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList.html

---

This class represents collection of properties of [Block](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block.html) class. Please check also base classes for other properties which are available for [Block](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block.html) objects: [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            **Eplan.EplApi.DataModel.BlockPropertyList**  
               [Eplan.EplApi.DataModel.ViewPartPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPartPropertyList.html)

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
[DefaultMember("Property")]
public class BlockPropertyList : PlacementPropertyList
```
```

```
```
[DefaultMember("Property")]
public ref class BlockPropertyList : public PlacementPropertyList
```
```

Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

- [C#](#i-tab-content-90dc1475-4125-4527-bc5d-7b126f22c3b5)

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
| Public Constructor | [BlockPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [INSTANCE\_ACTIVE\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_ACTIVE_PROPERTYSET().html) | Property arrangement # 19307. |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_FULLPLACEMENTLOCATION().html) | Placement # 19007. |
| Public Property | [INSTANCE\_PAGEFULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_PAGEFULLNAME().html) | Page name (full) # 19023. |
| Public Property | [INSTANCE\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_PAGENAME().html) | Page name # 19022. |
| Public Property | [INSTANCE\_PAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_PAGETYPE().html) | Page type # 19020. |
| Public Property | [INSTANCE\_PATHID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_PATHID().html) | Column number # 19005. |
| Public Property | [INSTANCE\_POSID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_POSID().html) | Row number # 19006. |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_TYPE().html) | Representation type / report type # 19021. |
| Public Property | [INSTANCE\_USER\_DEFINED\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_USER_DEFINED_PROPERTYSET().html) | User-defined property arrangement: Name # 19008. |
| Public Property | [INSTANCE\_XCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_XCOORD().html) | X coordinate # 19002. |
| Public Property | [INSTANCE\_YCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~INSTANCE_YCOORD().html) | Y coordinate # 19003. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of BlockPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |

[Top](#top)




See Also

#### Reference

[BlockPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BlockPropertyList_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[Block Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block.html)
  
[PlacementPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)