# IsVariableValid Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~IsVariableValid.html

---

Verifies the correctness if a variable name of a placeholder. If a variable name contains invalid characters, this method \returns false.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool IsVariableValid( 
   string strVariableName
)
```
```

```
```
public:
virtual bool IsVariableValid( 
   String^ strVariableName
)
```
```

#### Parameters

*strVariableName*
:   variable name to check.

#### Return Value

false: If strVariableName contains characters, which cannot be used for variable name. true: strVariableName can be used as variable name.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Service couldn't be correctly executed. Pleas see the exception message for further explanation. |



See Also

#### Reference

[PlaceHolder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html)
  
[PlaceHolder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder_members.html)