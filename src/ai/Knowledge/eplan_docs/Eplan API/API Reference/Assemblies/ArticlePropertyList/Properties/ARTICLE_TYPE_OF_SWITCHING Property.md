# ARTICLE_TYPE_OF_SWITCHING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_SWITCHING().html

---

Circuit type # 26547.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_TYPE_OF_SWITCHING {get; set;}

public:

property PropertyValue^ ARTICLE_TYPE_OF_SWITCHING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The way in which an electrical device or a component is connected in a circuit. Combination of the different switching possibilities of primary and secondary voltage windings. Example: Switching, cross-connection, etc.
