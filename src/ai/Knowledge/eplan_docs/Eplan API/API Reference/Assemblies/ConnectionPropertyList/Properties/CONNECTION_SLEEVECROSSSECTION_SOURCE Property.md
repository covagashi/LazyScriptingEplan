# CONNECTION_SLEEVECROSSSECTION_SOURCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SLEEVECROSSSECTION_SOURCE().html

---

Source: Sleeve cross-section # 31053.

Syntax

**C#**
**C++/CLI**


public PropertyValue CONNECTION_SLEEVECROSSSECTION_SOURCE {get; set;}

public:

property PropertyValue^ CONNECTION_SLEEVECROSSSECTION_SOURCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

If the connection is closed with a conductor sleeve, specify the cross-section of the sleeve here. This property is required for the transfer to packaging machines.
