# FUNC_ARTICLE_STANDARD_BACNET_ Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1257.html

---

Starting current, max. # 26191.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_STARTING_CURRENT_A( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_STARTING_CURRENT_A {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum starting current of electrical consumers.
