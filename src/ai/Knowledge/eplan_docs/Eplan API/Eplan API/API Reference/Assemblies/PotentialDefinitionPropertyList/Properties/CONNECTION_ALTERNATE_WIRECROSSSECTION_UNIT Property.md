# CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic420.html

---

Unit for alternative connection cross-section / diameter # 31065.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_ALTERNATE_WIRECROSSSECTION_UNIT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

The alternative unit belonging to the alternative cross-section/diameter of the connection. Has to be entered manually and enables you to display the connection cross-section / diameter in parallel in different units. Possible values are:

0 = As in project

1 = mmÂ²

2 = sqmm

3 = AWG

4 = mm

5 = KCM

6 = MCM

7 = Zoll

8 = "

9 = inch

10 = Âµm

11 = kcmil

12 = ÂµmÂ².



See Also

#### Reference

[PotentialDefinitionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList.html)
  
[PotentialDefinitionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinitionPropertyList_members.html)
  
[Overload List](topic1974.html)