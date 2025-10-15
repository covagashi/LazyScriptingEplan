# INTRINSICSAFETY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~INTRINSICSAFETY().html

---

Intrinsically safe # 31030.

Syntax

**C#**
**C++/CLI**


public PropertyValue INTRINSICSAFETY {get; set;}

public:

property PropertyValue^ INTRINSICSAFETY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Functions, connections, and connection definition points are defined as intrinsically safe using this property. The intrinsic safety at the function forces intrinsic safety at the associated connection points for which intrinsic safety is possible.
