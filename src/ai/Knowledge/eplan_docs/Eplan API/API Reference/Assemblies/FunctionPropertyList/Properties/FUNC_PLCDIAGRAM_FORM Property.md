# FUNC_PLCDIAGRAM_FORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCDIAGRAM_FORM().html

---

PLC diagram form # 20187.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCDIAGRAM_FORM {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLCDIAGRAM_FORM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This allows PLC cards (the PLC boxes) to each be assigned a separate report (a PLC diagram). The form set for the main function is only taken into account when generating reports.

If you assign a value using the Application Programming Interface, please ensure that the relevant master data exist in the project.
