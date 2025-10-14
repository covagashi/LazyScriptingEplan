# FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic693.html

---

Connection point pattern: Terminal designation # 36071.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Terminal designation, used in the connection point patterns of topology functions.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER.html)