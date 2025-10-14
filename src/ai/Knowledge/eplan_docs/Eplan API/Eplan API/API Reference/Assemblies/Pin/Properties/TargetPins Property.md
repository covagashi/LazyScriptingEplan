# TargetPins Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TargetPins.html

---

Returns Pin objects of other functions connected directly with this conn. point.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Pin[] TargetPins {get;}
```
```

```
```
public:
property array<Pin^>^ TargetPins {
   array<Pin^>^ get();
}
```
```

Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.



See Also

#### Reference

[Pin Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html)
  
[Pin Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin_members.html)