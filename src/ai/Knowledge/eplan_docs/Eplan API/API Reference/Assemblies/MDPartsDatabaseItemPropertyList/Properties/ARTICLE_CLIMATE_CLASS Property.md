# ARTICLE_CLIMATE_CLASS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CLIMATE_CLASS().html

---

Climate class # 26407.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_CLIMATE_CLASS {get; set;}

public:

property MDPropertyValue^ ARTICLE_CLIMATE_CLASS {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification of the environmental climatic conditions, i.e. air temperature, humidity and pressure at specific operating locations, that may occur during operation (including downtimes), storage or transportation on land or at sea. Maintenance and repair conditions are not included.
