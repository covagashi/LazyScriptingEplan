# GetOptionByName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup~GetOptionByName.html

---

Returns [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) assigned to the OptionGroup with given name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Option GetOptionByName( 
   string strName
)
```
```

```
```
public:
Option^ GetOptionByName( 
   String^ strName
)
```
```

#### Parameters

*strName*
:   name of the option to find

#### Return Value

[Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) assigned to the OptionGroup that has passed strName.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |



See Also

#### Reference

[OptionGroup Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html)
  
[OptionGroup Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup_members.html)