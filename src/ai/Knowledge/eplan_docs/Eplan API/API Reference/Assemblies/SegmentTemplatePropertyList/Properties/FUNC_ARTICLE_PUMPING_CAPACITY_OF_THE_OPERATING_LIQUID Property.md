# FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1237.html

---

Transport volume # 26329.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_PUMPING_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PUMPING_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of the material or liquid that can or should be conveyed.
