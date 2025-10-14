# FUNC_PLC_IGNORE_BUSADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLC_IGNORE_BUSADDRESS().html

---

Ignore missing bus ID # 20412.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLC_IGNORE_BUSADDRESS {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLC_IGNORE_BUSADDRESS {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

This settings possibility is designed for devices in bus systems that do not require a bus ID. If this property is activated at a bus port, the missing bus ID is ignored during the execution of check run 004037, and no check run message is issued for this bus port.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLC_IGNORE_BUSADDRESS.html)