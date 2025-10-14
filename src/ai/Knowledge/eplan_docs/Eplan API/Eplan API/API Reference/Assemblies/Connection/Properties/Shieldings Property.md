# Shieldings Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Shieldings.html

---

Returns the Shielding objects the connection is composed of. It does not return Shielding objects the connection is shielded by.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Function[] Shieldings {get;}
```
```

```
```
public:
property array<Function^>^ Shieldings {
   array<Function^>^ get();
}
```
```

#### Property Value

Array of Shielding objects of function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the Shielding objects. |



See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)
  
[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)