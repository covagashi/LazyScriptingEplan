# ARTICLE_LIFETIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_LIFETIME().html

---

Service time # 22142.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_LIFETIME {get; set;}

public:

property PropertyValue^ ARTICLE_LIFETIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The time during which a technical system or object can be used without exchanging core components or a complete breakdown.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.
