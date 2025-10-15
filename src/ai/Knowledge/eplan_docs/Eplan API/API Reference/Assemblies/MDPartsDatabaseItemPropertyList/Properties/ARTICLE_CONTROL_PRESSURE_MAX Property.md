# ARTICLE_CONTROL_PRESSURE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CONTROL_PRESSURE_MAX().html

---

Pilot pressure, max. # 26150.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_CONTROL_PRESSURE_MAX {get; set;}

public:

property MDPropertyValue^ ARTICLE_CONTROL_PRESSURE_MAX {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum pressure that a pneumatic or hydraulic system can use to control a device or component. This value is usually specified in bar or pascal. Maximum pressure for actuating fluid power valves with a pneumatic or pilot-controlled electrical actuating device.
