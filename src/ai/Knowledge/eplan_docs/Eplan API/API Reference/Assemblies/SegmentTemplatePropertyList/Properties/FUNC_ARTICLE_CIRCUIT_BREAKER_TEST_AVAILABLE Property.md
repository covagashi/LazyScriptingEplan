# FUNC_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1120.html

---

Closing pressure # 26552.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_CLOSING_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CLOSING_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Pressure to close an item under defined conditions.
