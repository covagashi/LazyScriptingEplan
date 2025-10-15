# ARTICLE_FREE_DATA_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_FREE_DATA_UNIT(Int32).html

---

Free properties: Unit # 22148.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_FREE_DATA_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_FREE_DATA_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Unit for the value of the free property. More than 1000 assignments can be made using the index.
