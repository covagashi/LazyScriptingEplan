# FUNC_ARTICLE_CURRENT_CONSUMPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION(Int32).html

---

Current consumption # 26596.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_CURRENT_CONSUMPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CURRENT_CONSUMPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The electric current in amperes (A) required for the normal operation of a device.
