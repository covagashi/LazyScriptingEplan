Execution of a command line expression.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

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

true: The command line operation was successfully completed. false: One or more errors occured while executing the command line operation.



See Also

#### Reference

[CommandLineInterpreter Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html)
  
[CommandLineInterpreter Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter_members.html)
  
[Overload List](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~Execute.html)