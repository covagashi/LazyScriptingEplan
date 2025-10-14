# NetConnectionPoints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint~NetConnectionPoints.html

---

Returns all PinBase objects of NetDefinitionPoint

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public NetDefinitionPoint.NetConnectionPoint[] NetConnectionPoints {get;}
```
```

```
```
public:
property array<NetDefinitionPoint.NetConnectionPoint^>^ NetConnectionPoints {
   array<NetDefinitionPoint.NetConnectionPoint^>^ get();
}
```
```

#### Property Value

All PinBases defined in NetDefinitionPoint

Remarks

`NetConnectionPoints` are [PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)s taken from [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html). Location of `NetConnectionPoints` is relative to the symbol's insertion point.



See Also

#### Reference

[NetDefinitionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint.html)
  
[NetDefinitionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint_members.html)