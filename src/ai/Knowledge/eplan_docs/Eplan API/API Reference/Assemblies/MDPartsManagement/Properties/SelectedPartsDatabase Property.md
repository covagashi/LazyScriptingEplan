# SelectedPartsDatabase Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~SelectedPartsDatabase.html

---

The parts database that is currently used.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPartsDatabase SelectedPartsDatabase {get; set;}
```
```

```
```
public:

property MDPartsDatabase^ SelectedPartsDatabase {

   MDPartsDatabase^ get();

   void set (    MDPartsDatabase^ value);

}
```
```

Remarks

Represents the database that is currently used and visible for example in parts management dialog. Setting the property has result even if a database was closed. The property does not get the parts database used in the parts navigator.
