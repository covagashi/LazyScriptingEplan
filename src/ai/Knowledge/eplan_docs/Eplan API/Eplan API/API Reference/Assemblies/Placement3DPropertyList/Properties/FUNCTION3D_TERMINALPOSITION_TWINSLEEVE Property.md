# FUNCTION3D_TERMINALPOSITION_TWINSLEEVE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic695.html

---

Connection point pattern: Dual sleeve prescribed # 36065.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_TWINSLEEVE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TWINSLEEVE {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Specifies for a connection point in the connection point pattern that dual sleeves are to be used if two connections lead to this connection point.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_TWINSLEEVE.html)