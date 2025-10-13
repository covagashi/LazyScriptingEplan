Deletes the specified right entry from the UserRights database (rights management dialog)

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public bool DeleteRight( 
   string strRightname
)
```
```

```
```
public:
bool DeleteRight( 
   String^ strRightname
)
```
```

#### Parameters

*strRightname*
:   name of the user right entry to remove

#### Return Value

true, in case the right was successfully removed from the rights management database.

Remarks

The currently logged-in user must have the URShowAdministrationDialog right, this is the right to work on user rights. Any group assignments of this right are removed.



See Also

#### Reference

[UserRights Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights.html)
  
[UserRights Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights_members.html)