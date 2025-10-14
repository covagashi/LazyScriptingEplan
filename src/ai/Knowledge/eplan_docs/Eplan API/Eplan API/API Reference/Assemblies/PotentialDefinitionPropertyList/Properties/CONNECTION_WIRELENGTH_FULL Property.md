# CONNECTION_WIRELENGTH_FULL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH_FULL().html

---

Connection: Length (full) # 31090.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_WIRELENGTH_FULL {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_WIRELENGTH_FULL {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Length of a connection with information about the unit. The full value with all decimal places is always stored; the value is not rounded up. This ensures precision is retained when converting to a different unit.



See Also

#### Reference

[PotentialDefinitionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)
  
[PotentialDefinitionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_WIRELENGTH_FULL.html)