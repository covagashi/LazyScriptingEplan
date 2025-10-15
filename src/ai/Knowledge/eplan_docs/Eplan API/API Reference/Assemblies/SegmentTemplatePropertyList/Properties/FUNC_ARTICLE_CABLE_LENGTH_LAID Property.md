# FUNC_ARTICLE_CABLE_LENGTH_LAID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1115.html

---

Cable length, max. # 26399.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_CABLE_LENGTH_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_LENGTH_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum length of a cable that is permissible for a specific application or installation. Example: An extension cable may not be longer than 50 m in order to be used safely.
