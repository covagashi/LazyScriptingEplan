# FUNCTION3D_TERMINALPOSITION_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic674.html

---

Connection point pattern: Routing direction # 36059.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_TERMINALPOSITION_DIRECTION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_TERMINALPOSITION_DIRECTION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Routing direction of an individual connection point in the connection point pattern, which is selected from a drop-down list.

0 = Automatic

1 = Move up

2 = Down

3 = Left

4 = Right.

The routing direction specifies the direction of the search for a possible entry point into a routing path network.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_DIRECTION.html)