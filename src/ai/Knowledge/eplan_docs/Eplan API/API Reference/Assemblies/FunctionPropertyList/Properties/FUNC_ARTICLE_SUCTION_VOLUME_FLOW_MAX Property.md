# FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX(Int32).html

---

Intake flow rate, max. # 26199.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum flow rate within the working range of the conveyed gas at the outlet point of a fluid machine in relation to the conditions prevailing at the inlet point for the total temperature, the total pressure and the gas composition (e.g. humidity).
