# Send Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventManager~Send.html

---

Sends an event to the system.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int Send( 

   string strEventName,

   IEventParameter pEventParameter

)
```
```

```
```
public:

int Send( 

   String^ strEventName,

   IEventParameter^ pEventParameter

)
```
```

#### Parameters

*strEventName*
:   Name of the event that is sent.

*pEventParameter*
:   Object containing parameters for this event.

#### Return Value

Status of event processing. The Status is a result value of an event. The value is defined by the catcher of the event. When more events are called, the result is a bitwise or of every single result.

Example

Send the EventAusCSharpAddIn event with string parameters being passed ([EventParameterString](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventParameterString.html))

- [C#](#i-tab-content-bb3656ed-05f6-4c6a-8505-c2fed964a064)

```
EventManager oEventManager = new EventManager();

EventParameterString oEventParamString = new EventParameterString();

oEventParamString.String = "ParameterAusCSharpAddIn";

long lRetVal = oEventManager.Send("EventAusCSharpAddIn", oEventParamString);



```
