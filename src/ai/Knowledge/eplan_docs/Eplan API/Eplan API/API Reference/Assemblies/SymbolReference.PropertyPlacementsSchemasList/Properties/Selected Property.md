# Selected Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Selected.html

---

Gets a PropertyPlacementsSchema object that represents the selected property placements configuration. Sets the current property placements configuration. Note: Changing the current property placements configuration deletes the existing property placements. This can make some API objects of type PropertyPlacement become invalid.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public SymbolReference.PropertyPlacementsSchema Selected {get; set;}
```
```

```
```
public:
property SymbolReference.PropertyPlacementsSchema^ Selected {
   SymbolReference.PropertyPlacementsSchema^ get();
   void set (    SymbolReference.PropertyPlacementsSchema^ value);
}
```
```



See Also

#### Reference

[SymbolReference.PropertyPlacementsSchemasList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList.html)
  
[SymbolReference.PropertyPlacementsSchemasList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList_members.html)