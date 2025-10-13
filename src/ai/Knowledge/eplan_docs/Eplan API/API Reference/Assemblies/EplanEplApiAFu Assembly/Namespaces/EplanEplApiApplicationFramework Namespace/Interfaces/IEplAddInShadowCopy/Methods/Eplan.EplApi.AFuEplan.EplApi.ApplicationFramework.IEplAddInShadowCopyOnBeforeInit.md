Called by the framework before [IEplAddIn.OnInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInit.html) and passes the location from which add-in assembly has been registered.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
void OnBeforeInit( 
   string strOriginalAssemblyPath
)
```
```

```
```
void OnBeforeInit( 
   String^ strOriginalAssemblyPath
)
```
```

#### Parameters

*strOriginalAssemblyPath*
:   Full path to location from which the add-in assembly has been registered.

Remarks

Any exception thrown by this method don't influence the initialization process. Such exception is wrapped and logged into System messages.



See Also

#### Reference

[IEplAddInShadowCopy Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy.html)
  
[IEplAddInShadowCopy Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy_members.html)