# ARTICLE_PERFORMANCE_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PERFORMANCE_DESCRIPTION().html

---

Performance description, standardized: Description (device, utility, service) # 26425.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_PERFORMANCE_DESCRIPTION {get; set;}

public:

property MDPropertyValue^ ARTICLE_PERFORMANCE_DESCRIPTION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

In the context of the standardized performance description, this is the descriptive text of the performance description for a device, a utility or a service.
