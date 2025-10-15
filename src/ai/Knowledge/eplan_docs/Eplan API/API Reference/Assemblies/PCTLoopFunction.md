# PCTLoopFunction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoopFunction.html

---

TODO

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)  
         **Eplan.EplApi.DataModel.Planning.PCTLoopFunction**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class PCTLoopFunction : PlanningSegment, Eplan.EplApi.DataModel.IArticleUser, Eplan.EplApi.DataModel.IWriteProtection
```
```

```
```
public ref class PCTLoopFunction : public PlanningSegment, Eplan.EplApi.DataModel.IArticleUser, Eplan.EplApi.DataModel.IWriteProtection
```
```



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PCTLoopFunction Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoopFunction~_ctor().html) | Default constructor. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArticleReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~ArticleReferences.html) | Returns [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by PlanningSegment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [CanHaveArticleData](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CanHaveArticleData.html) | Check if the PlanningSegment can have [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [Children](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Children.html) | Returns all children of this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Functions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Functions.html) | Returns array of functions and 3d functions assigned to this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [IsArticleDataReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsArticleDataReadOnly.html) | Determines whether the article reference data can be changed for this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [IsFixedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~IsFixedDevice.html) | Set or checks if device of this function is fixed. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [LinkedSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~LinkedSegments.html) | Returns all linked segments for this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [LinkedWithSuperiorSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~LinkedWithSuperiorSegments.html) | Returns all superior segments for this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [LocalTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~LocalTemplates.html) | Returns set of local templates assigned to this object or to its segment template. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Macro.html) | Macro file with window or page macros, used when placing the macro. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Name.html) | Returns the name of planning segment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Pages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Pages.html) | Returns collection of all pages assigned to the planning segment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Parent.html) | Gets or Sets parent object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [PLCAddresses](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PLCAddresses.html) | Returns array of PLC inputs and outputs for this planning object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoopFunction~Properties.html) | EPLAN properties of the PCTLoopFunction object. |
| Public Property | [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentDefinition.html) | Returns the [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) of the PlanningObject. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentPlacement.html) | Returns placed representation of this planning segment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) | Segment template assigned to this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [SortId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SortId.html) | Number used to sort elements in current branch of planning tree. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [TemplatesFromArticles](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~TemplatesFromArticles.html) | Returns set of templates from articles assigned to this object or to its segment template. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~WriteProtected.html) | Check if object is currently write protected or sets Manual write protection (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddArticleReference.html) | Overloaded. Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the PlanningSegment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [AddLocalTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddLocalTemplate.html) | Add new local template based on function definition. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [AddPLCAddress](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddPLCAddress.html) | Overloaded. Creates copy of existing PLC inputs or outputs for this planning object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [CollectStructureProperties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CollectStructureProperties.html) | Returns [Eplan.EplApi.DataModel.FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html). (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [CreateLink](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateLink.html) | Creates a link between two given PlanningSegments. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [DeleteLink](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~DeleteLink.html) | Deletes a link from this object that links given targetSegment. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of PCTLoopFunction object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [PlaceAt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceAt.html) | Places the segment onto the given page, in the given location. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [PlaceMacroAt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~PlaceMacroAt.html) | Places a macro on a given page. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Remove.html) | Removes object from PlanningSegment with all its children. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [RemoveArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveArticleReference.html) | Removes the ArticleReference from the PlanningSegment (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [RemoveLocalTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveLocalTemplate.html) | Removes a local template from this object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [RemovePLCAddress](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemovePLCAddress.html) | Removes existing PLC input or output from this planning object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [RevertToTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RevertToTemplate.html) | Restores information stored in template to planning object. (Inherited from [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |

[Top](#top)
