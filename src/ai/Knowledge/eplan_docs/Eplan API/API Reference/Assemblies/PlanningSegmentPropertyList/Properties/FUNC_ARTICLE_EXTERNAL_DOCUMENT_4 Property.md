# FUNC_ARTICLE_EXTERNAL_DOCUMENT_4 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic925.html

---

Part: External document 5 # 20264.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_EXTERNAL_DOCUMENT_5( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_DOCUMENT_5 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

Outputs the "External document 5" property of the nth part using the index.
