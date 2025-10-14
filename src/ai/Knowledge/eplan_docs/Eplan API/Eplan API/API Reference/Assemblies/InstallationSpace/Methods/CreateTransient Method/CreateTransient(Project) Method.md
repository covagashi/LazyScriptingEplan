# CreateTransient(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace~CreateTransient(Project).html

---

Creates transient InstallationSpace object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CreateTransient( 
   Project oProject
)
```
```

```
```
public:
void CreateTransient( 
   Project^ oProject
)
```
```

#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the InstallationSpace cannot be created. |



See Also

#### Reference

[InstallationSpace Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html)
  
[InstallationSpace Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace~CreateTransient.html)