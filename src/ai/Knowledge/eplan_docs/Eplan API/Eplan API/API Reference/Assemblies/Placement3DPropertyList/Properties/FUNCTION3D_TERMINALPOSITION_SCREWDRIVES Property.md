# FUNCTION3D_TERMINALPOSITION_SCREWDRIVES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic690.html

---

Socket size # 36094.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_SCREWDRIVES( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_SCREWDRIVES {
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

Describes the form of the screw head for applying a screwdriver or a wrench. Enter of, for example PZ 1 or PH 1 or TX 5 or 0.5x3.0.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_SCREWDRIVES.html)