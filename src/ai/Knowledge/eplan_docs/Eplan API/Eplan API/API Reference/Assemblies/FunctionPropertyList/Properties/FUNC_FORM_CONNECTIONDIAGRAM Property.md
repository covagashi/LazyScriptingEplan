# FUNC_FORM_CONNECTIONDIAGRAM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_FORM_CONNECTIONDIAGRAM().html

---

Form for wiring diagram # 20234.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_FORM_CONNECTIONDIAGRAM {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_FORM_CONNECTIONDIAGRAM {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Allows for a separate form for wiring diagrams to be stated at the main function of a device. Wiring diagrams consist of several connection diagrams and are used to output information about connected conductors and targets. (Additional information can be obtained in the help system in the section "Generating wiring diagrams".)

If you assign a value via the API interface, please make sure that the corresponding master data is available in the project.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_FORM_CONNECTIONDIAGRAM.html)