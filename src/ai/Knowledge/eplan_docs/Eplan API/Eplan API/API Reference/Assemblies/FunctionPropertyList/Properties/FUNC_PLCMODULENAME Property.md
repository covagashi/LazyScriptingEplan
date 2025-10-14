# FUNC_PLCMODULENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCMODULENAME().html

---

PLC card name # 20437.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCMODULENAME {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCMODULENAME {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Name of a PLC card (identifying for PLC devices during PLC data exchange in the AutomationML AR APC or Studio 5000 Architect format). The property can be displayed in reports and used as a filter criterion in the navigators. Depending on whether the PLC box represents a PLC card, a rack or a CPU, the PLC card name must be unique within a rack, a station or a configuration project.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCMODULENAME.html)