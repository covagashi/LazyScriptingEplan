# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~Create.html

---

Creates a new Group3D object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 
   Placement3D[] placement3Ds
)
```
```

```
```
public:
void Create( 
   array<Placement3D^>^ placement3Ds
)
```
```

#### Parameters

*placement3Ds*
:   3D placements that form the 3D group.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.InsufficientElementsCountException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientElementsCountException.html) | Thrown when the number of 3D placements is less than two. |



See Also

#### Reference

[Group3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D.html)
  
[Group3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D_members.html)