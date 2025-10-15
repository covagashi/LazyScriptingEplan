# FUNC_ARTICLE_RANGE_OF_APPLICATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_RANGE_OF_APPLICATION(Int32).html

---

Operating area # 26286.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_RANGE_OF_APPLICATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RANGE_OF_APPLICATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Recommended area of use, e.g., indoor or outdoor area.
