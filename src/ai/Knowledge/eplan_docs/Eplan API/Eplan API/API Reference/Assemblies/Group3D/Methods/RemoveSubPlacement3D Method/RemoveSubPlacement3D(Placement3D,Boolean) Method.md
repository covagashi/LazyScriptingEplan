# RemoveSubPlacement3D(Placement3D,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3D(Placement3D,Boolean).html

---

Removes [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) from the 3D group and from the project. The Placement3D object passed into this method is no longer valid.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void RemoveSubPlacement3D( 
   Placement3D placement3D,
   bool removeEmptyGroup3D
)
```
```

```
```
public:
virtual void RemoveSubPlacement3D( 
   Placement3D^ placement3D,
   bool removeEmptyGroup3D
)
```
```

#### Parameters

*placement3D*
:   3D placement removed from the 3D group and from the project.

*removeEmptyGroup3D*
:   If true, the Group3D object will be removed also when it becomes empty.



See Also

#### Reference

[Group3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D.html)
  
[Group3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~RemoveSubPlacement3D.html)
  
[Placement3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)