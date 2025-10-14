# CreateTransient(SymbolVariant,Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CreateTransient(SymbolVariant,Project).html

---

Creates a Function. It is not placed on any [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). Its category is taken from [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static Function CreateTransient( 
   SymbolVariant symbVariant,
   Project proj
)
```
```

```
```
public:
static Function^ CreateTransient( 
   SymbolVariant^ symbVariant,
   Project^ proj
)
```
```

#### Parameters

*symbVariant*
:   [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) the Function will be assigned

*proj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `symbVariant` is `null`. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the function has already been created. |



See Also

#### Reference

[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[Function Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CreateTransient.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[SymbolVariant Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html)