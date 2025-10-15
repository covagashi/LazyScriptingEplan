# FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic153.html

---

Dynamic viscosity range: End value # 26300.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Highest value of the dynamic viscosity specified for a particular product or material. The dynamic viscosity is a measure of the viscosity of a fluid and is measured in pascal seconds (Pa·s).
