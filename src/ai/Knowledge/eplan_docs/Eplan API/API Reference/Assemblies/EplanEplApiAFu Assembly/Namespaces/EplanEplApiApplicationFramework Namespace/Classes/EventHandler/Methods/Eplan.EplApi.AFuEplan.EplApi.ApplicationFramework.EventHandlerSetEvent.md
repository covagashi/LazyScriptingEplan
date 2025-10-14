Defines for which event the [IEplanEvents](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEvents.html) is raised.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetEvent( 
   string strEventName
)
```
```

```
```
public:
void SetEvent( 
   String^ strEventName
)
```
```

#### Parameters

*strEventName*
:   Events with this name are edited through this event handler object.

Example

Define the event to respond to

* [C#](#i-tab-content-8b5966d8-c1ef-414f-ab73-d1c399927558)

```
// Generate an event handler object
Eplan.EplApi.ApplicationFramework.EventHandler myHandler= new Eplan.EplApi.ApplicationFramework.EventHandler();
// The program should respond to this event
myHandler.SetEvent("onActionStart.String.*");
```