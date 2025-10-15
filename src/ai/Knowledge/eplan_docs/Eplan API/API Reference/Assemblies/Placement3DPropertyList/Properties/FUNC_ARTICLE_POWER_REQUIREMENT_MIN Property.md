# FUNC_ARTICLE_POWER_REQUIREMENT_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MIN(Int32).html

---

Power requirement, min. # 26424.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_POWER_REQUIREMENT_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POWER_REQUIREMENT_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum quantity of energy that a device or plant requires to function properly.
