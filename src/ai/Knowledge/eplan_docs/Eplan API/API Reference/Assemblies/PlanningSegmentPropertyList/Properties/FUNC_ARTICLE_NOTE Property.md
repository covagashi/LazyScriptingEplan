# FUNC_ARTICLE_NOTE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_NOTE(Int32).html

---

Part description # 31014.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_NOTE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOTE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Description of the part, carried over from parts management. Using the index, you can differentiate between 50 entries.
