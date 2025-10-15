# ARTICLE_CURRENT_CARRYING_CAPACITY_MAX_PER_I_O_SIGNAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1547.html

---

Current carrying capacity (per I/O signal), max. # 26155.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_CURRENT_CARRYING_CAPACITY_MAX_PER_I_O_SIGNAL {get; set;}

public:

property MDPropertyValue^ ARTICLE_CURRENT_CARRYING_CAPACITY_MAX_PER_I_O_SIGNAL {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum electric current in amperes (A) that a single input / output signal (PLC I/O connection point) can safely carry without overheating or damage.
