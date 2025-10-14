# CONNECTION_MLWIRENUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_MLWIRENUMBER().html

---

Connection: Color (multilingual) # 31061.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_MLWIRENUMBER {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_MLWIRENUMBER {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Stores the connection color as a multilingual text. The color code is taken from the "Connection color / number" property (or the "Color / number" field of the property dialog) and is assigned to a color corresponding to the assignment table in the project settings. It is case-sensitive. The property is automatically updated with every change to the connection color / number.



See Also

#### Reference

[PotentialDefinitionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)
  
[PotentialDefinitionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList~CONNECTION_MLWIRENUMBER.html)