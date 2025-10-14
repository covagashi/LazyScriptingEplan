# FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic659.html

---

Thermal design: Simultaneity factor (automatic) # 36044.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR_AUTOMATIC {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Is required for calculating the power dissipation. Displays the value of the simultaneity factor (if it exists). Otherwise the value from the project settings is used.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2080.html)