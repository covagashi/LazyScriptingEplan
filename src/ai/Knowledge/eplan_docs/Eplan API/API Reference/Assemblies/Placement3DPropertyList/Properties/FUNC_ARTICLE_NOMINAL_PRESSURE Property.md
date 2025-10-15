# FUNC_ARTICLE_NOMINAL_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_NOMINAL_PRESSURE(Int32).html

---

Nominal pressure # 26471.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_NOMINAL_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum permissible pressure that an item or piping can withstand under normal operating conditions. This pressure is specified in bar.
