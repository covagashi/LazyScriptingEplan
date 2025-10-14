# FunctionDefinition Constructor(FunctionDefinitionLibrary,FunctionCategory,Int16,Int16)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic209.html

---

Constructs and initializes a FunctionDefinition object with the specified function's category, group and ID. Note: The specified function definition must exist in the function definitions library passed by the funcDefLibrary parameter

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public FunctionDefinition( 
   FunctionDefinitionLibrary funcDefLibrary,
   FunctionCategory funcCategory,
   short funcGroup,
   short funcID
)
```
```

```
```
public:
FunctionDefinition( 
   FunctionDefinitionLibrary^ funcDefLibrary,
   FunctionCategory funcCategory,
   short funcGroup,
   short funcID
)
```
```

#### Parameters

*funcDefLibrary*
:   A function definition library object.

*funcCategory*
:   Category of the function definition.

*funcGroup*
:   Group identifier of the function definition.

*funcID*
:   Identifier of the function definition.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the specified function definition (category, group and ID) doesn't exists in the library. |



See Also

#### Reference

[FunctionDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html)
  
[FunctionDefinition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~_ctor.html)