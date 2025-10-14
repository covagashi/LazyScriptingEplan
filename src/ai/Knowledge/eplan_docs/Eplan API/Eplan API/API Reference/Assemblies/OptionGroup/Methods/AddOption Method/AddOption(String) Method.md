# AddOption(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup~AddOption(String).html

---

Adds [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) to the OptionGroup. The description is set to an empty multilang value, the state is set to true (so the option is active).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Option AddOption( 
   string strName
)
```
```

```
```
public:
Option^ AddOption( 
   String^ strName
)
```
```

#### Parameters

*strName*
:   name of the option

#### Return Value

Returns added Option.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |
| [System.ArgumentException](#) | Thrown when `Option` with `strName` already exists in OptionGroup. |

Remarks

Option name must be unique for the group.



See Also

#### Reference

[OptionGroup Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html)
  
[OptionGroup Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup~AddOption.html)