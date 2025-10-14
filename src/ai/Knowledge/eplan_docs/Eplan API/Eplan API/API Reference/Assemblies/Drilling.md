# Drilling

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling.html

---

Class represents drilling objects in P8.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)  
         [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)  
            **Eplan.EplApi.DataModel.E3D.Drilling**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class Drilling : Function3D, Eplan.EplApi.DataModel.IArticleUser, Eplan.EplApi.DataModel.IFunctionBase, Eplan.EplApi.DataModel.IPropertyPlacementsContainer
```
```

```
```
public ref class Drilling : public Function3D, Eplan.EplApi.DataModel.IArticleUser, Eplan.EplApi.DataModel.IFunctionBase, Eplan.EplApi.DataModel.IPropertyPlacementsContainer
```
```

Remarks

Type of drilling is determined by its function definition and additionally by its ItemType.  
  
Corresponding FunctionCategory for this class is CabVirtNC.



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Drilling Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~_ctor().html) | Default constructor. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AbsoluteTransformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformation.html) | Absolute position and rotation represented by transformation matrix. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [AbsoluteTransformationOfMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformationOfMacro.html) | Absolute position and rotation represented by transformation matrix where transformation of macro is considered. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [AreConnectionPointPositionsLocal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AreConnectionPointPositionsLocal.html) | Determines if connection point data are saved locally at the part placement. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [ArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~ArticleReferences.html) | Returns [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [Articles](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~Articles.html) | Returns [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Function3D, and only those that are stored in project database. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [CanHaveArticleData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~CanHaveArticleData.html) | Check if the Function3D can have [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [Children](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Children.html) | Returns all children of this object. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [Color](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Color.html) | Color of 3D Placement (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [Connection3Ds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Connection3Ds.html) | All existing 3d connections whose beginning or end is this placement. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [ConnectionPointPositions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~ConnectionPointPositions.html) | Array of connection points data. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [ContourName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~ContourName.html) | Name of the drilling contour. |
| Public Property | [Corners](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Corners.html) | Represents coordinates of corners (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [CreatedAutomatically](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreatedAutomatically.html) | Determine if object was create automatically by P8. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FunctionDefinition.html) | Returns the [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [Group3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Group3D.html) | Returns a Group3D object that the Placement3D object belongs to. If the Placement3D object doesn't belong to any group3D, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~InstallationSpace.html) | Returns [InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) in which this object exists. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~IsFixedDevice.html) | Set or checks if device of this Function3d is fixed. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [IsHidden](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsHidden.html) | Indicates whether object is currently hidden in 3D editor view. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsMeshCreated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsMeshCreated.html) | Returns `true` if a mesh is created for this objects and assigned for it. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [IsNameEmpty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~IsNameEmpty.html) | Returns true if the list of name's properties is empty (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsPlaced.html) | Returns true if the placement is placed. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ItemType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~ItemType.html) | Item type of this Function3D, corresponds to value of the 'Item' list in GUI. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [Layer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Layer.html) | Returns the [Eplan.EplApi.DataModel.Graphics.GraphicalLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) of the Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [Mesh](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~Mesh.html) | Returns mesh. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~Name.html) | Returns the name of the Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [NameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~NameParts.html) | Name of the Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Parameter1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Parameter1.html) | Parameter1. |
| Public Property | [Parameter2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Parameter2.html) | Parameter2. |
| Public Property | [Parameter3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Parameter3.html) | Parameter3. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Parent.html) | Gets or Sets parent placement. Caution: The Change of the parent will also change the absolute position because Placement3D stores the position relative to his parent (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [PlacementArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PlacementArea.html) | Represents placement area of a Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [Planes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Planes.html) | Returns children of this object which are [Plane](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane.html). (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~PlanningSegment.html) | [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) assigned to this function3d. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Properties.html) | .NET Property enabling access to EPLAN properties of the Drilling object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacements.html) | Returns [Placement3D.PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacementsSchemas.html) assigned to this Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacementsSchemas.html) | Returns [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [RelativeTransformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformation.html) | Position and rotation relative to the parent placement represented by transformation matrix. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [RelativeTransformationOfMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformationOfMacro.html) | Relative position and rotation represented by transformation matrix where transformation of macro is considered. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [TopLevelParent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~TopLevelParent.html) | Gets the root 3d placement from tree of 3d elements which this object is part of. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [UseLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~UseLocalPropertyPlacements.html) | Return true if the instance uses the local property instances, otherwise it uses the ones of the variant. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Property | [VisibleName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~VisibleName.html) | Returns the visible name of the Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Property | [VisibleNameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~VisibleNameParts.html) | Returns visible name of the Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~AddArticleReference.html) | Overloaded. Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Function3D. Returns the added [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html). (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Method | [AddConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddConnectionPointPosition.html) | Creates new connection point position. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [AddMatePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddMatePersistent.html) | Add copy of a mate to a Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~CopyTo.html) | Copy 3D Placement Placement3D and its children will be copied into the same Project as newParent Then parent of the copy will be set to newParent new parent of copy (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Methodstatic (Shared in Visual Basic) | [CreateChamferedRectangle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateChamferedRectangle.html) | Overloaded. Creates new chamfer rectangle drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateChamferedRectangleTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateChamferedRectangleTransient.html) | Creates new transient chamfer rectangle drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateContour](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateContour.html) | Overloaded. Creates a new drilling in the shape of the given contour. |
| Public Methodstatic (Shared in Visual Basic) | [CreateContourTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateContourTransient.html) | Creates a new transient drilling in the shape of the given contour. |
| Public Methodstatic (Shared in Visual Basic) | [CreateHexagon](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateHexagon.html) | Overloaded. Creates new hexagon drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateHexagonTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateHexagonTransient.html) | Creates new transient hexagon drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateOctagon](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateOctagon.html) | Overloaded. Creates new octagon drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateOctagonTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateOctagonTransient.html) | Creates new transient octagon drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateRectangle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRectangle.html) | Overloaded. Creates new rectangle drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateRectangleTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRectangleTransient.html) | Creates new transient rectangle drilling |
| Public Methodstatic (Shared in Visual Basic) | [CreateRound](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRound.html) | Overloaded. Creates unplaced new round drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateRoundedRectangle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRoundedRectangle.html) | Overloaded. Creates new rounded rectangle drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateRoundedRectangleTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRoundedRectangleTransient.html) | Creates new transient rounded rectangle drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateRoundTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateRoundTransient.html) | Creates transient unplaced new round drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateSlot](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateSlot.html) | Overloaded. Creates new slot drilling in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateSlotTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateSlotTransient.html) | Creates new transient slot drilling. |
| Public Methodstatic (Shared in Visual Basic) | [CreateTapHole](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateTapHole.html) | Overloaded. Creates new tap hole in project. |
| Public Methodstatic (Shared in Visual Basic) | [CreateTapHoleTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateTapHoleTransient.html) | Creates new tap hole in project. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Drilling object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [FindSourceMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindSourceMate.html) | Overloaded. Find source mate by name. Mate namePlacement optionsConsider child mounting surfaces (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [FindTargetMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindTargetMate.html) | Overloaded. Find target mate by name. Mate nameConsider mounting clearanceConsider child mounting surfaces (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBox.html) | Returns bounding box of a Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [GetBoundingBoxRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBoxRelative.html) | Returns relative bounding box of a Placement3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetSourceMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetSourceMates.html) | Overloaded. Get array of all source mates from this object. Placement optionsConsider child mounting surfaces (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [GetTargetMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetTargetMates.html) | Overloaded. Get array of all target mates from this object. Consider mounting clearanceConsider child mounting surfaces (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetValidItemTypes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~GetValidItemTypes.html) | Returns an array of item types valid for this Function3D. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Move.html) | Move this object. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [MoveRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~MoveRelative.html) | Move this object relative to its parent. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Remove.html) | Removes object from project and all its children. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~RemoveArticleReference.html) | Removes the ArticleReference from the Function. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Method | [RemoveConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemoveConnectionPointPosition.html) | Removes connection point data stored under given index. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [RemovePlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemovePlacement.html) | Removes object and all its children only from layout space. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [SetParent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SetParent.html) | Sets parent placement. Sets parent placement. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [SetPlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~SetPlanningSegment.html) | Assigns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) to this function3d. (Inherited from [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~StoreConnectionPointPosition.html) | Stores data from connection point position in function under given index. (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag (Inherited from [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [updateDrilling](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~updateDrilling.html) | Updates the drilling (especially his height). |

[Top](#top)




See Also

#### Reference

[Drilling Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling_members.html)
  
[Eplan.EplApi.DataModel.E3D Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D_namespace.html)