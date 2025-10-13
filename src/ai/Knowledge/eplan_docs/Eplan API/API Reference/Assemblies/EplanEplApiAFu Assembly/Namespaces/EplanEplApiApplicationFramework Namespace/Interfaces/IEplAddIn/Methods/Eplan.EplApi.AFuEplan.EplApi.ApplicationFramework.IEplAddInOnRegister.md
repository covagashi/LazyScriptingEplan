Is called once when a new add-in is selected.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
bool OnRegister( 
   ref bool bLoadOnStart
)
```
```

```
```
bool OnRegister( 
   bool% bLoadOnStart
)
```
```

#### Parameters

*bLoadOnStart*
:   true: The module is loaded at system startup and OnInit() is called.

#### Return Value

true, if the add-in was successfully loaded and registered.

Remarks

When this function returns false, the add-in is not added to the system. At next start of EPLAN the add-in is not loaded. If bLoadOnStart is set to false, the API add-in assembly is registered but not loaded automatically on the next startup of EPLAN. Still all actions registered with the add-in are known in EPLAN and the add-in will be loaded once one of the actions is executed. Please mind, that in this case OnInitGui(), etc. is only called, when the dll is loaded, so normal ribbon items from the add-in are not created, when EPLAN starts.



See Also

#### Reference

[IEplAddIn Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn.html)
  
[IEplAddIn Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn_members.html)