# FUNC_CABLE_DESTINATION_WITH_PLCPLUG_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic618.html

---

Cables: Target (with plug designation) # 20385.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CABLE_DESTINATION_WITH_PLCPLUG_DESIGNATION {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_CABLE_DESTINATION_WITH_PLCPLUG_DESIGNATION {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the target of the cable with plug designation. At bus ports the bus interface name of the bus port is displayed in addition to the plug designation. The property can be used for the display in the schematic as well as in block properties, at external editing and in reports.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2053.html)