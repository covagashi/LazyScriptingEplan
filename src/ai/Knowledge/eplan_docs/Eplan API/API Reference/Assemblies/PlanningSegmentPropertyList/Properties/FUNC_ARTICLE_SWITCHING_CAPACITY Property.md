# FUNC_ARTICLE_SWITCHING_CAPACITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1042.html

---

Temperature (medium), max. # 26610.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_TEMPERATUR_MEDIUM_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TEMPERATUR_MEDIUM_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum temperature that a medium (such as a liquid or a gas) can reach while flowing through a device or component without causing damage or impairing its functionality.
