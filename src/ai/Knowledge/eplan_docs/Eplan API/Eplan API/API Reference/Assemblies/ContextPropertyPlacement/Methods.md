# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement_methods.html

---

For a list of all members of this type, see [ContextPropertyPlacement members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Methodstatic (Shared in Visual Basic) | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~Create.html) | Overloaded. Creates and inserts it into a group ContextPropertyPlacement which displays symbol properties. |
| Public Method | [CreateFromPageProperties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~CreateFromPageProperties.html) | Creates and insert into page ContextPropertyPlacement which displays page property. |
| Public Method | [CreateFromProjectProperties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~CreateFromProjectProperties.html) | Creates and insert into page ContextPropertyPlacement which displays project property. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [DockText](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~DockText.html) | Docks one text to another. You can see how it works in GUI. Select element on schematic, display properties, show property placements and dock / undock them. (Inherited from [Eplan.EplApi.DataModel.Graphics.TextBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~GetBoundingBox.html) | Overloaded. Overridden. Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. |
| Public Method | [GetDisplayString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~GetDisplayString.html) | Returns formated display string of the content (Inherited from [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetIsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~GetIsVisible.html) | Returns the property placement visibility in symbol editor, for the given scheme. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetVisibilityDependingOnLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~SetVisibilityDependingOnLayer.html) | This method sets the visibility of the graphical instance to depend on the layer setting (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreWithSymbolPropertyPlacementSchema](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~StoreWithSymbolPropertyPlacementSchema.html) | Stores property placement with given scheme to symbol variant. |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [UndockText](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~UndockText.html) | Undock text from another oner one. You can see how it works in GUI. Select element on schematic, display properties, show property placements and dock / undock them. (Inherited from [Eplan.EplApi.DataModel.Graphics.TextBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase.html)) |

[Top](#top)

See Also

#### Reference

[ContextPropertyPlacement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)