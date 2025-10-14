# FUNC_PLCAUTOPLUG_AND_CONNPTDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCAUTOPLUG_AND_CONNPTDESIGNATION().html

---

Connection point designation (with plug designation (automatic)) # 20183.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCAUTOPLUG_AND_CONNPTDESIGNATION {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCAUTOPLUG_AND_CONNPTDESIGNATION {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Combined property from the plug designation (automatic) and connection point designation of a PLC connection point or device connection point, separated by a colon. At bus ports the bus interface name of the bus port is displayed in addition to the plug designation.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCAUTOPLUG_AND_CONNPTDESIGNATION.html)