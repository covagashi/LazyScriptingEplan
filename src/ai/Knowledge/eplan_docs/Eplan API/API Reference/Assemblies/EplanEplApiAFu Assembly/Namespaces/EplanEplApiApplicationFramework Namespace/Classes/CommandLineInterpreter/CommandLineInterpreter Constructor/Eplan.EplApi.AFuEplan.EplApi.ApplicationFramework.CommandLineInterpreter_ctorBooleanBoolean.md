constructor

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public CommandLineInterpreter( 
   bool bEnableExceptions,
   bool bCollectSysMessages
)
```
```

```
```
public:
CommandLineInterpreter( 
   bool bEnableExceptions,
   bool bCollectSysMessages
)
```
```

#### Parameters

*bEnableExceptions*
:   If true then, if an exception raised, it will be transmitted to the caller. If false, only a boolean value will be returned by calling Execute method. If this returned value is false, this means the action has not succeed. Otherwise all things are OK.

*bCollectSysMessages*
:   If true then system messages will be collected by Execute method in ActionCallingContext.SysMessages.

Remarks

The type of exceptions which can be raised, if parameter bEnableExceptions=true, is from System::BaseException.


