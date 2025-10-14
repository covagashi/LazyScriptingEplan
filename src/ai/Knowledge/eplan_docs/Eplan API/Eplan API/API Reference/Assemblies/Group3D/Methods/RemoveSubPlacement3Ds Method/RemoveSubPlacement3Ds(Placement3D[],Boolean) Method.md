# RemoveSubPlacement3Ds(Placement3D[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3Ds(Placement3D[],Boolean).html

---

Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s from the 3D group and from the project. The Placement3D objects passed into this method are no longer valid.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void RemoveSubPlacement3Ds( 
   Placement3D[] placement3Ds,
   bool removeEmptyGroup3D
)
```
```

```
```
public:
virtual void RemoveSubPlacement3Ds( 
   array<Placement3D^>^ placement3Ds,
   bool removeEmptyGroup3D
)
```
```

#### Parameters

*placement3Ds*
:   3D placements removed from the 3D group and from the project.

*removeEmptyGroup3D*
:   If true, the method will remove also the Group3D object when it becomes empty.



See Also

#### Reference

[Group3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D.html)
  
[Group3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3Ds.html)
  
[Placement3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)