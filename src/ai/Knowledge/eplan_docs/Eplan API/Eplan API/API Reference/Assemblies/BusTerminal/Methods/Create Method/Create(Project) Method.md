# Create(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.BusTerminal~Create(Project).html

---

Creates an unplaced BusTerminal object of category **Eplan.EplApi.DataModel.Function.Enums.Category.PLCTerminal**, group id `4` and id `1`.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 
   Project pProject
)
```
```

```
```
public:
void Create( 
   Project^ pProject
)
```
```

#### Parameters

*pProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `pProject` is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |



See Also

#### Reference

[BusTerminal Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.BusTerminal.html)
  
[BusTerminal Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.BusTerminal_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.BusTerminal~Create.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)