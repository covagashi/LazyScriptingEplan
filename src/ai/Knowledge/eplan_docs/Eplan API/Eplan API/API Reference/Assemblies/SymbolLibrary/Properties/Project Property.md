# Project Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary~Project.html

---

Returns the project to which the StorableObject belongs.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override Project Project {get;}
```
```

```
```
public:
property Project^ Project {
   Project^ get() override;
}
```
```

#### Property Value

The project to which the StorableObject belongs,

`null` if the StorableObject is transient or if the StorableObject does not belong to the objects of the project (PropertyPlacement with default scheme).



See Also

#### Reference

[SymbolLibrary Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary.html)
  
[SymbolLibrary Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibrary_members.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)