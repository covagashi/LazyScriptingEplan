# CONNECTION_SLEEVECROSSSECTION_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic122.html

---

Target: Sleeve cross-section # 31054.

Syntax

**C#**
**C++/CLI**


public PropertyValue CONNECTION_SLEEVECROSSSECTION_DESTINATION {get; set;}

public:

property PropertyValue^ CONNECTION_SLEEVECROSSSECTION_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

If the connection is closed with a conductor sleeve, specify the cross-section of the sleeve here. This property is required for the transfer to packaging machines.
