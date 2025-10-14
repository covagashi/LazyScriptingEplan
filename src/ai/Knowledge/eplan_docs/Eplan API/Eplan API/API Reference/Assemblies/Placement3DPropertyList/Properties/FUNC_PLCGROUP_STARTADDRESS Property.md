# FUNC_PLCGROUP_STARTADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_STARTADDRESS().html

---

Start address of PLC card # 20419.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCGROUP_STARTADDRESS {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

The value entered here specifies the start value for the address range of a PLC card. At the same time the addressing of the inputs and outputs of this card begins with the start value entered here. This value can also be used as the configuration value for readdressing PLC configurations. For a card that has both inputs and outputs, specify the start value of the inputs here. The property is entered on the "PLC box" tab of the property dialog.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_STARTADDRESS.html)