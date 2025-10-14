# Project Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html

---

Returns the project to which the StorableObject belongs.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual Project Project {get;}
```
```

```
```
public:
virtual property Project^ Project {
   Project^ get();
}
```
```

#### Property Value

The project to which the StorableObject belongs,

`null` if the StorableObject is transient or if the StorableObject does not belong to the objects of the project (PropertyPlacement with default scheme).



See Also

#### Reference

[StorableObject Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)
  
[StorableObject Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject_members.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)