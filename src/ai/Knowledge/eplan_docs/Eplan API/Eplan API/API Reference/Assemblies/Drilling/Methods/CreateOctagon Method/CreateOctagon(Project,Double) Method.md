# CreateOctagon(Project,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateOctagon(Project,Double).html

---

Creates new octagon drilling in project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CreateOctagon( 
   Project pProject,
   double dEdgeLength
)
```
```

```
```
public:
void CreateOctagon( 
   Project^ pProject,
   double dEdgeLength
)
```
```

#### Parameters

*pProject*


*dEdgeLength*
:   Length of one edge of the drilling. Must be greater than 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Drilling has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pProject` is `null`. |
| [System.ArgumentException](#) | Thrown if edge length isn't greater than 0. |



See Also

#### Reference

[Drilling Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling.html)
  
[Drilling Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~CreateOctagon.html)