# GetEnabled Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetEnabled.html

---

Returns whether an action is enabled

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool GetEnabled( 

   ActionCallingContext oCallingContext,

   string strActionWithParameters

)
```
```

```
```
public:

bool GetEnabled( 

   ActionCallingContext^ oCallingContext,

   String^ strActionWithParameters

)
```
```

#### Parameters

*oCallingContext*
:   Used to pass parameters to an action and to receive return values of the action

*strActionWithParameters*
:   Action name with parameters

Remarks

Is used to enable/dissable control bound to the action (usually RibbonCommand)
