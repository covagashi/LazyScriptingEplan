# FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic933.html

---

Mounting length: Protective tube # 26278.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_FITTING_LENGTH_OF_THE_PROTECTION_TUBE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FITTING_LENGTH_OF_THE_PROTECTION_TUBE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Mounting length of the protective tube (in mm).
