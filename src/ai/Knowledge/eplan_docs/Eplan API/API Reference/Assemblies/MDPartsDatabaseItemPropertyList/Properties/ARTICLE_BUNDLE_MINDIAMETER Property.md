# ARTICLE_BUNDLE_MINDIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_BUNDLE_MINDIAMETER().html

---

Minimum bundle diameter # 22260.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_BUNDLE_MINDIAMETER {get; set;}

public:

property MDPropertyValue^ ARTICLE_BUNDLE_MINDIAMETER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

The minimum bundle diameter indicates the minimum diameter of a bundle of connections that must be met in order to bundle it with this part (e.g., a cable tie or spiral coiled tube).
