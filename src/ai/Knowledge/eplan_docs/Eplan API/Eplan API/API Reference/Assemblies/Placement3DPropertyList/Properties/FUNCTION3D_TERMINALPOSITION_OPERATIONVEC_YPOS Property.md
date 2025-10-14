# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YPOS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic686.html

---

Y position: Tool # 36089.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YPOS( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YPOS {
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

The properties for specifying coordinate values for the position of the tool describe the position of a terminal screw in an item with screw connection. Entry for example "12 mm".



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2101.html)