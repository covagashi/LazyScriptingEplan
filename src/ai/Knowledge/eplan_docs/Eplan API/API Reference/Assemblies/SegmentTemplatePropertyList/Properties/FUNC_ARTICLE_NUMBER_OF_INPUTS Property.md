# FUNC_ARTICLE_NUMBER_OF_INPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1197.html

---

Number of outputs # 31177.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_NUMBER_OF_OUTPUTS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NUMBER_OF_OUTPUTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of outputs.
