# DimensionGroup

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup.html

---

This class represents DimensionGroup on the page.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)  
            **Eplan.EplApi.DataModel.DimensionGroup**

Syntax

**C#**
**C++/CLI**


public class DimensionGroup : Group, IPlacementsContainer

public ref class DimensionGroup : public Group, IPlacementsContainer

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DimensionGroup Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~_ctor().html) | Constructor. When object created with this constructor, its `create` method must be call. |

[Top](#top)

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DimensionType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~DimensionType.html) | Gets type of DimensionGroup. |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Location.html) | Get or set the placement's location. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~Properties.html) | .NET Property enabling access to P8 properties of the Page object. |
| Public Property | [SubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~SubPlacements.html) | Returns all grouped [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~Create.html) | Overloaded. Creates DimensionGroup on a given page. |
| Public Method | [DeepUnGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~DeepUnGroup.html) | Overloaded. Remove all [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group and it's sub groups. If true method will remove also SubGroups. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [InsertSubPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacement.html) | Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) to a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [InsertSubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacements.html) | Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s to a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [IsEditable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsEditable.html) | Check if the Group is editable. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [IsGroupValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsGroupValid.html) | Returns true, if group is valid if not, the group should be dissolved (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Move.html) | Moves the group (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [RemoveSubPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacement.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) from the group and from the project. The Placement object passed into this method is no longer valid. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [RemoveSubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacements.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s from the group and from the project. The Placement objects passed into this method are no longer valid. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [UnGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |

[Top](#top)
