# OnRegister Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~OnRegister.html

---

The action can be registered under a name determined by the action and an overload level.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
bool OnRegister( 
   ref string Name,
   ref int Ordinal
)
```
```

```
```
bool OnRegister( 
   String^% Name,
   int% Ordinal
)
```
```

#### Parameters

*Name*
:   Name under which the action is registered in the system. Note\: Action names with . are not allowed.

*Ordinal*
:   Overload level of action

#### Return Value

true: the return parameters are valid. false: the action is registered under the name of the class that implements this interface;



See Also

#### Reference

[IEplAction Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html)
  
[IEplAction Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction_members.html)