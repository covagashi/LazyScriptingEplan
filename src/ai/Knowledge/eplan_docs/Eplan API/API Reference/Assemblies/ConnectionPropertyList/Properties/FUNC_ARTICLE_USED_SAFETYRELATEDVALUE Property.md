# FUNC_ARTICLE_USED_SAFETYRELATEDVALUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_USED_SAFETYRELATEDVALUE(Int32).html

---

Safety-related values: Use case in use # 20307.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_USED_SAFETYRELATEDVALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_USED_SAFETYRELATEDVALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Indicates the use case that is used for the safety-related values of a part.
