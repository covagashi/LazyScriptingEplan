# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZDIR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic687.html

---

Z vector: Tool # 36093.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZDIR( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZDIR {
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

The properties for the vector of the tool describe the position and the screwing direction of a terminal screw in an item with screwed connection. Entry for example "-1".



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2102.html)