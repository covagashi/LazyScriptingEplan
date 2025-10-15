# BaseMate Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~BaseMate.html

---

Default target mate for this Plane.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PlaneMate BaseMate {get;}
```
```

```
```
public:

property PlaneMate^ BaseMate {

   PlaneMate^ get();

}
```
```

#### Property Value

Returns target mate or `null` if mate does not exist.

Remarks

When snapping an item by a base mate, it is set as a child of a target Placement3D Also the orientation of an item is adjusted to a target Placement3D
