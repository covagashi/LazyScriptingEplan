# FUNC_ARTICLE_POSITION_NUMBER_STLB Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic991.html

---

Possible uses # 26290.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_POSSIBLE_APPLICATIONS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POSSIBLE_APPLICATIONS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Application areas or types of usage for which a product or a component is suitable. Example: Residential area, industry, office.
