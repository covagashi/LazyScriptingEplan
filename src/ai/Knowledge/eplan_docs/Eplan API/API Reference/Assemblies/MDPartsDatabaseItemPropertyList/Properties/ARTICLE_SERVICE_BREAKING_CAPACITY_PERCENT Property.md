# ARTICLE_SERVICE_BREAKING_CAPACITY_PERCENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1674.html

---

Service short-circuit breaking capacity (Ics as % of Icu) # 26592.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_SERVICE_BREAKING_CAPACITY_PERCENT {get; set;}

public:

property MDPropertyValue^ ARTICLE_SERVICE_BREAKING_CAPACITY_PERCENT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

"Ics as % of Icu" describes the relative breaking capacity in relation to the maximum load capacity "Icu". The value of "Ics as % of Icu" indicates the percentage of the rated ultimate short-circuit breaking capacity "Icu" that the power circuit-breaker can safely disconnect during normal operation. The service short-circuit breaking capacity "Ics" is the maximum current that a power circuit-breaker can safely and repeatedly disconnect under short-circuit conditions without being damaged. A higher percentage means greater reliability and safety in operation.
