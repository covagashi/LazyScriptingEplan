# Set(PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Set(PointD).html

---

Sets [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) value in PropertyValue object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue Set( 
   PointD pnt
)
```
```

```
```
public:
PropertyValue^ Set( 
   PointD pnt
)
```
```

#### Parameters

*pnt*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) to convert

#### Return Value

This object is returned.

Remarks

In case this `PropertyValue` object was create by user only the local value of this object will be change/set.

If this `PropertyValue` object was accrued from property list or from `StorableObject` then also value in original location will be changed.



See Also

#### Reference

[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[PropertyValue Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Set.html)