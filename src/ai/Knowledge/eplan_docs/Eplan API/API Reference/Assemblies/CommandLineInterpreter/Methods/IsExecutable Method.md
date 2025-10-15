# IsExecutable Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~IsExecutable.html

---

Checks whether the execution of an expression is possible.  
This is only the case when the corresponding action is available.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool IsExecutable( 

   string strExpression

)
```
```

```
```
public:

virtual bool IsExecutable( 

   String^ strExpression

)
```
```

#### Parameters

*strExpression*
:   Command line expression to be checked.

#### Return Value

â¢ TRUE if the command line expression is valid  
â¢ FALSE if the command line expression cannot be executed
