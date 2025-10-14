# FUNC_CABLE_ALTERNATE_CROSSSECTION_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_ALTERNATE_CROSSSECTION_UNIT().html

---

Cable / Conduit: Unit for alternative cross-section / diameter # 20126.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CABLE_ALTERNATE_CROSSSECTION_UNIT {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_CABLE_ALTERNATE_CROSSSECTION_UNIT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

The alternative unit for the alternative cross-section / diameter of the cable or conduit. Has to be entered manually and enables you to specify the cross-section / diameter simultaneously in different units. Possible values are:

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

For pipes and hoses in fluid power and process engineering the property refers to the inner diameter.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_ALTERNATE_CROSSSECTION_UNIT.html)