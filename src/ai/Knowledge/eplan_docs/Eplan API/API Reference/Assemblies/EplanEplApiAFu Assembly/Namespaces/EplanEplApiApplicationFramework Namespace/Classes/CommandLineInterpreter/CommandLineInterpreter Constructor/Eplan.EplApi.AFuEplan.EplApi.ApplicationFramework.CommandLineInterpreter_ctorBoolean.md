constructor

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public CommandLineInterpreter( 
   bool bEnableExceptions
)
```
```

```
```
public:
CommandLineInterpreter( 
   bool bEnableExceptions
)
```
```

#### Parameters

*bEnableExceptions*
:   If true then, if an exception raised, it will be transmitted to the caller. If false, only a boolean value will be returned by calling Execute method. If this returned value is false, this means the action has not succeed. Otherwise all things are OK.

Remarks

The type of exceptions which can be raised, if parameter bEnableExceptions=true, is from System::BaseException.



See Also

#### Reference

[CommandLineInterpreter Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html)
  
[CommandLineInterpreter Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter_members.html)
  
[Overload List](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~_ctor.html)