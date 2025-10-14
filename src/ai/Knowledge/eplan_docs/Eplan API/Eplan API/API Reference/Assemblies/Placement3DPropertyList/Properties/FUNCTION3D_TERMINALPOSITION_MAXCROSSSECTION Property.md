# FUNCTION3D_TERMINALPOSITION_MAXCROSSSECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic676.html

---

Connection point pattern: Max. cross-section # 36063.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_MAXCROSSSECTION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_MAXCROSSSECTION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Maximum connection cross-section to be connected for a connection point in the connection point pattern.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2092.html)