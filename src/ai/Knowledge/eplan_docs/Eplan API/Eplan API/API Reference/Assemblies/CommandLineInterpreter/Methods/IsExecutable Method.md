# IsExecutable Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~IsExecutable.html

---

Checks whether the execution of an expression is possible. This is only the case when the corresponding action is available.

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

true, if command line expression is valid false, if command line expression cannot be executed.



See Also

#### Reference

[CommandLineInterpreter Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html)
  
[CommandLineInterpreter Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter_members.html)