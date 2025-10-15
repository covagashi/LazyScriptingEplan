# ARTICLE_SUBCRAFT_PROCESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUBCRAFT_PROCESS(Int32).html

---

Subtrade 'Process engineering' # 22197.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_SUBCRAFT_PROCESS( 

   int index

) {get; set;}

public:

property PropertyValue^ ARTICLE_SUBCRAFT_PROCESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 20.

This property can be used to create several subtrades for a trade.
