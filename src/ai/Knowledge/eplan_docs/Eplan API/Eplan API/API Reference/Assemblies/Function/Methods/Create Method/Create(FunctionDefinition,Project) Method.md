# Create(FunctionDefinition,Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create(FunctionDefinition,Project).html

---

Creates a not placed Function from [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) passed as parameter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static Function Create( 
   FunctionDefinition pFunctionDefinition,
   Project pProject
)
```
```

```
```
public:
static Function^ Create( 
   FunctionDefinition^ pFunctionDefinition,
   Project^ pProject
)
```
```

#### Parameters

*pFunctionDefinition*
:   [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) used to create the Function.

*pProject*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the Function will be located in.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the function cannot be created. |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |

Example

Example shows how to create function with help of function definition:

- [C#](#i-tab-content-4c2f6d18-6b29-4c6e-acaa-8427515818a3)

```

//create function object based on function definition
Function oNewFunction = Function.Create(oFuncDef, oPage.Project);

//place created function on page
oNewFunction.Page = oPage;


```

See Also

#### Reference

[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[Function Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Create.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[FunctionDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html)