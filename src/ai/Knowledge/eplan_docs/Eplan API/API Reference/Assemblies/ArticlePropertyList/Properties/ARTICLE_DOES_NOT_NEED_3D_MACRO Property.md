# ARTICLE_DOES_NOT_NEED_3D_MACRO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOES_NOT_NEED_3D_MACRO().html

---

Part does not require a 3D macro # 22392.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_DOES_NOT_NEED_3D_MACRO {get; set;}

public:

property PropertyValue^ ARTICLE_DOES_NOT_NEED_3D_MACRO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Specifies that the part does not require a macro representation for the 3D mounting layout. This means that the "Graphical macro" property can remain empty for the part.
