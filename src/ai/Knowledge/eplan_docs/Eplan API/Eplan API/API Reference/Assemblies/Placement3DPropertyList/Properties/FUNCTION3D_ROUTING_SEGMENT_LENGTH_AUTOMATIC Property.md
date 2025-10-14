# FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic662.html

---

Routing path / Curve: Length (automatic) # 36028.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Length of a routing path or curve placed in the layout space. Is used during routing to calculate the precise length of the associated connection. Shows the content of the manually entered length or, when that is empty, the geometric length in the layout space.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2082.html)