Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html).

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public delegate long EventHandlerNameFunctionResult( 
   IEventParameter pIEventParameter,
   string strNameOfEvent
)
```
```

```
```
public delegate int64 EventHandlerNameFunctionResult( 
   IEventParameter^ pIEventParameter,
   String^ strNameOfEvent
)
```
```

#### Parameters

*pIEventParameter*


*strNameOfEvent*
:   The original name of the send event. Can be useful when I was registered for an wildcard event, p.e. "Test\*"

#### Return Value

the return value of your event. When there are more handlers the result value is the bitwise or of all results.



See Also

#### Reference

[EventHandlerNameFunctionResult Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerNameFunctionResult.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)