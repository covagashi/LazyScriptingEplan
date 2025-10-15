# FUNC_PLCPLUG_AND_CONNPTDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCPLUG_AND_CONNPTDESIGNATION().html

---

Connection point designation (with plug designation) # 20435.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_PLCPLUG_AND_CONNPTDESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_PLCPLUG_AND_CONNPTDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Combined property from the plug designation and connection point designation of a PLC connection point or device connection point, separated by a colon. At bus ports the bus interface name of the bus port is displayed in addition to the plug designation.
