# FUNC_ARTICLE_EXTERNAL_DOCUMENT_14 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic916.html

---

Part: External document 15 # 20274.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_EXTERNAL_DOCUMENT_15( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_DOCUMENT_15 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "External document 15" property of the nth part using the index.
