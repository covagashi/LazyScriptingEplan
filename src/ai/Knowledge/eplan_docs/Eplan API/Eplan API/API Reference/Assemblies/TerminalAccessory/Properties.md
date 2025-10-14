# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory_properties.html

---

For a list of all members of this type, see [TerminalAccessory members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Article.html) | Returns the article of this articlereference. This is the Article stored in the Project, can be NULL if the article is not found in Project. (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [BelongsToArticlePlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~BelongsToArticlePlacement.html) | Returns true, if the article reference contains to an article placement (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [Count](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Count.html) | Sets and gets count (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [FunctionTemplates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~FunctionTemplates.html) | Returns an array of transient object (of Connection or Function type) that represent function templates associated with the article referenced by this object. (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [IdentifyingName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~IdentifyingName.html) | Gets the identifying device tag of the parent function(property ArticleReferencePropertyList.ARTICLEREF\_IDENTNAME). (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [IsAssembly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~IsAssembly.html) | Represents this reference an assembly (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ParentObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~ParentObject.html) | Returns the Object this ArticleReference belongs to. (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [PartNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~PartNr.html) | Returns ArticleReference's part number. (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [PartNumber](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory~PartNumber.html) | Gets part number |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Properties.html) | Represents ArticleReference properties (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |
| Public Property | [ReferencePos](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory~ReferencePos.html) | Gets position in the reference table of the object (means propertyindex) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Variant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory~Variant.html) | Gets variant |
| Public Property | [VariantNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~VariantNr.html) | Sets and gets ArticleReference's variant number. (Inherited from [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) |

[Top](#top)

See Also

#### Reference

[TerminalAccessory Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory.html)
  
[Eplan.EplApi.DataModel.EObjects Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects_namespace.html)
  
[TerminalStrip Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)
  
[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)