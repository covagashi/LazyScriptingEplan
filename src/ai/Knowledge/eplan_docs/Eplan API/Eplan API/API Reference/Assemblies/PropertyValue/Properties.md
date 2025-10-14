# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue_properties.html

---

For a list of all members of this type, see [PropertyValue members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Definition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Definition.html) | Returns an object that provides information about the property and its definition. The information includes: name of the property, its data type, whether it's indexed or not, whether it's read-only, upper/lower bounds of values for numerical properties. To use the Definition property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Id.html) | Returns the P8 property descriptor (id and index) that the object points to. To use the Id property, the PropertyValue object must point to a project property (persistent property). Transient PropertyValue objects don't have descriptors because they point directly to a value. A transient PropertyValue is created by operator and takes values of base types. |
| Public Property | [Indexes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Indexes.html) | Returns the valid / actually used indexes. It can be used with the PropertyValue::operator []. To use the Indexes property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [IsEmpty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~IsEmpty.html) | Checks if the property is empty. If it's not, it could be read. IMPORTANT: If property is indexed you have to set the index. |
| Public Property | [Item](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Item.html) | Returns or sets the object of a persistent [PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) which points to a specific index. To use the Item property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [LastUsedIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~LastUsedIndex.html) | Returns the number of the highest used index. Indexes start at 1. If the property is not indexed or there is no used index, LastUsedIndex is 0. To use the LastUsedIndex property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Parent.html) | Property list to which this property value is connected. |

[Top](#top)

See Also

#### Reference

[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionBasePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html)
  
[InterruptionPointPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList.html)
  
[LocationBoxPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationBoxPropertyList.html)
  
[PagePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html)
  
[PlacementPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)
  
[SymbolVariantPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariantPropertyList.html)
  
[ProjectPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html)
  
[ConnectionDefinitionPointPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList.html)
  
[DocumentBasePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentBasePropertyList.html)