# Assign Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Assign.html

---

Assigns this function to another, which means that values of this function's properties are copied to the target object and the function itself is removed from the project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Assign( 
   Function target
)
```
```

```
```
public:
void Assign( 
   Function^ target
)
```
```

#### Parameters

*target*
:   The target object whose properties are set with values from this function.

Remarks

\* This method corresponds to the 'Assign' action called from the device navigator's context menu. \* After the assignment, this object becomes the target object.



See Also

#### Reference

[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[Function Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function_members.html)