# FUNC_ARTICLE_INRUSH_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_INRUSH_CURRENT(Int32).html

---

Inrush current # 26296.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_INRUSH_CURRENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INRUSH_CURRENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Electrical current that flows when the device is switched on.
