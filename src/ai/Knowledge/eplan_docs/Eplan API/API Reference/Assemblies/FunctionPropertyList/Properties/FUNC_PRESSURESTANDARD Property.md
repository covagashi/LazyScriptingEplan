# FUNC_PRESSURESTANDARD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PRESSURESTANDARD().html

---

Pressure level # 20330.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_PRESSURESTANDARD {get; set;}

public:

property PropertyValue^ FUNC_PRESSURESTANDARD {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The nominal pressure of a pipe system specifies a reference value. The designation PN ("Pressure Nominal") is used, followed by a whole number without dimensions that indicates the design pressure in bar at room temperature (20° C). The permissible pressure is correspondingly smaller at higher temperatures, depending on the permissible material characteristics (yield point).
