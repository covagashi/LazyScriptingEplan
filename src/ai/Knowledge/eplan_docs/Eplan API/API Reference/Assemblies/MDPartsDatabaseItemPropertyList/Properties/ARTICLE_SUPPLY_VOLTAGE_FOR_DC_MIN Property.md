# ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN().html

---

Supply voltage (DC), min. # 26170.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum DC voltage that may be applied to the supply input of a device temporarily or continuously in order for the device to function correctly. This voltage is specified in volts (V).
