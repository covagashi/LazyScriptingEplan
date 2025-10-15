# FUNC_ARTICLE_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CAPACITY(Int32).html

---

Volume capacity # 26323.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_CAPACITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CAPACITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Usable volume of the container.
