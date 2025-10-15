# Execute(String,ActionCallingContext) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~Execute(String,ActionCallingContext).html

---

Execution of a command line expression

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool Execute( 

   string strExpression,

   ActionCallingContext oContext

)
```
```

```
```
public:

virtual bool Execute( 

   String^ strExpression,

   ActionCallingContext^ oContext

)
```
```

#### Parameters

*strExpression*
:   Action plus arguments

*oContext*
:   The context assigned to the action. Additional data can be encapsulated by the user here.

#### Return Value

â¢ TRUE if the command line operation was completed successfully  
â¢ FALSE if one or more errors occured while executing the command line operation
