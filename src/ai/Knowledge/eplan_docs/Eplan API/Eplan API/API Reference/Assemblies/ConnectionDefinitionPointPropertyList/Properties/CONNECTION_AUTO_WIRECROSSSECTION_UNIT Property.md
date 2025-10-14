# CONNECTION_AUTO_WIRECROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic117.html

---

Unit for connection cross-section / diameter (automatic) # 31060.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_AUTO_WIRECROSSSECTION_UNIT {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_AUTO_WIRECROSSSECTION_UNIT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Automatically determined units of the connection cross-section or diameter. Possible values are:

0 = Undefined

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

[ConnectionDefinitionPointPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList.html)
  
[ConnectionDefinitionPointPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList_members.html)
  
[Overload List](topic1805.html)