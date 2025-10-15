# FUNC_ARTICLE_POSITION_KEYWORD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1215.html

---

Item number (manufacturer) # 26535.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_POSITION_NUMBER_MANUFACTURER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POSITION_NUMBER_MANUFACTURER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Unique identification or identification number of the product in the product catalog of the manufacturer.
