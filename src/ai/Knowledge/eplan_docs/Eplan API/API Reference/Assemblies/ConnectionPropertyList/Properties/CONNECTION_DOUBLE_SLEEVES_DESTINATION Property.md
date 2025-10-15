# CONNECTION_DOUBLE_SLEEVES_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_DOUBLE_SLEEVES_DESTINATION().html

---

Dual sleeve prescribed at 2 targets at the target # 31099.

Syntax

**C#**
**C++/CLI**


public PropertyValue CONNECTION_DOUBLE_SLEEVES_DESTINATION {get; set;}

public:

property PropertyValue^ CONNECTION_DOUBLE_SLEEVES_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is activated during routing if the "Dual sleeve prescribed" (ID 35560) property is activated for the connection point at the target of the connection.
