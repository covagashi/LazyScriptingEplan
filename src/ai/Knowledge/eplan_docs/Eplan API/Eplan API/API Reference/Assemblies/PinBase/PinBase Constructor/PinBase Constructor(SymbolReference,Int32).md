# PinBase Constructor(SymbolReference,Int32)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~_ctor(SymbolReference,Int32).html

---

Creates a PinBase object representing a graphical connection point of a symbol and initializes Index, Parent, Direction and Location properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PinBase( 
   SymbolReference smbl,
   int pinIdx
)
```
```

```
```
public:
PinBase( 
   SymbolReference^ smbl,
   int pinIdx
)
```
```

#### Parameters

*smbl*
:   SymbolReference object which gives a symbol variant for initialization of the Direction and Location properties. May be NULL.

*pinIdx*
:   Index of this connection point among the symbol's connection points.



See Also

#### Reference

[PinBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)
  
[PinBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~_ctor.html)