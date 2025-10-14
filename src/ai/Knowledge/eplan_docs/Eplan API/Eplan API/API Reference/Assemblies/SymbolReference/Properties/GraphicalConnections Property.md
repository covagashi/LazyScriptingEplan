# GraphicalConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnections.html

---

An array of [SymbolReference.GraphicalConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+GraphicalConnection.html) objects representing all auto-connecting lines connected to the pins of the symbol. This property may be useful to check graphical layout of connections associated with the symbol (including T-nodes, corners, etc.).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public SymbolReference.GraphicalConnection[] GraphicalConnections {get;}
```
```

```
```
public:
property array<SymbolReference.GraphicalConnection^>^ GraphicalConnections {
   array<SymbolReference.GraphicalConnection^>^ get();
}
```
```



See Also

#### Reference

[SymbolReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)
  
[SymbolReference Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference_members.html)
  
[SymbolReference.GraphicalConnection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+GraphicalConnection.html)