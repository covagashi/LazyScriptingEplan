# FUNC_PLCADDRESSRANGE_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCADDRESSRANGE_2().html

---

Address range 2 (SIEMENS STEP 7 Classic) # 20299.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCADDRESSRANGE_2 {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCADDRESSRANGE_2 {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

For PLC cards that have both inputs and outputs, you can use this property to specify a separate address range for the outputs. The property is entered on the "PLC box" tab of the property dialog. For this property to be reported during addressing, the Separate address range for inputs and outputs check box must be deactivated in the PLC-specific settings.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCADDRESSRANGE_2.html)