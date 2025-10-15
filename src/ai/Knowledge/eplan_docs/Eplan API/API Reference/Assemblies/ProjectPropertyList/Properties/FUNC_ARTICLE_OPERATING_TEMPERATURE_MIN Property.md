# FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN(Int32).html

---

Operating temperature, min. # 26242.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_OPERATING_TEMPERATURE_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum temperature at which a device can be operated safely and reliably.
