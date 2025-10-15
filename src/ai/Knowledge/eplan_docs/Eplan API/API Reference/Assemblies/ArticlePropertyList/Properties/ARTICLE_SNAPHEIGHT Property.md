# ARTICLE_SNAPHEIGHT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SNAPHEIGHT().html

---

Clip-on height # 22211.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_SNAPHEIGHT {get; set;}

public:

property PropertyValue^ ARTICLE_SNAPHEIGHT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

The clip-on height describes the position in the side view or from the top / bottom. When it is placed on a mounting rail, the item is automatically placed on the rail to the correct mounting depth. If the rail is replaced, the item will "move" to the top. The item is thus aligned above the top edge on the basis of the value entered here, rather than on the underside of the rail.
