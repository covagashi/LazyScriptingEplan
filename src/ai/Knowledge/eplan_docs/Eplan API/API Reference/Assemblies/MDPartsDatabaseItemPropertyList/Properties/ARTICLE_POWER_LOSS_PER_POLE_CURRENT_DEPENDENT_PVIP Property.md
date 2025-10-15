# ARTICLE_POWER_LOSS_PER_POLE_CURRENT_DEPENDENT_PVIP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1655.html

---

Power dissipation (per pole), current-dependent # 26159.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_POWER_LOSS_PER_POLE_CURRENT_DEPENDENT_PVIP {get; set;}

public:

property MDPropertyValue^ ARTICLE_POWER_LOSS_PER_POLE_CURRENT_DEPENDENT_PVIP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Power dissipation (electrical heat losses) caused by the flow of current through a single pole of a device. This power dissipation is specified in watts (W) and depends on the current flowing through. Example: In the case of a fused load disconnect switch the power dissipation per pole is approximately 1.5 W at a rated current of 63 A.
