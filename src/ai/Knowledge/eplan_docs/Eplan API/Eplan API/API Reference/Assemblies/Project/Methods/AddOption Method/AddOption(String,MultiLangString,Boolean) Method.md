# AddOption(String,MultiLangString,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOption(String,MultiLangString,Boolean).html

---

Adds [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) to the `Project`.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Option AddOption( 
   string strName,
   MultiLangString mlDescription,
   bool bIsActive
)
```
```

```
```
public:
Option^ AddOption( 
   String^ strName,
   MultiLangString^ mlDescription,
   bool bIsActive
)
```
```

#### Parameters

*strName*
:   name of the option

*mlDescription*
:   multilang description of the option

*bIsActive*

#### Return Value

Returns added Option.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |
| [System.ArgumentNullException](#) | Thrown when `mlDescription` is `null`. |
| [System.ArgumentException](#) | Thrown when `Option` with `strName` already exists in Project. |

Remarks

This method adds an `Option` straight to the `Project`, Option is not assigned to any `OptionGroup`. Option name must be unique in the set of Options that are not assigned to any `OptionGroup`.



See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOption.html)