# Execute Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~Execute.html

---

Called by the framework when the action is to be performed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
bool Execute( 
   ActionCallingContext oActionCallingContext
)
```
```

```
```
bool Execute( 
   ActionCallingContext^ oActionCallingContext
)
```
```

#### Parameters

*oActionCallingContext*
:   Parameter for this call, see [ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html).

#### Return Value

true, if the action was successfully performed; true, if the action was successfully registered in the system.



See Also

#### Reference

[IEplAction Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html)
  
[IEplAction Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction_members.html)