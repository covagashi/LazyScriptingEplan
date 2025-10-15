# FUNC_PLCSAFETYUPPERBOUNDADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSAFETYUPPERBOUNDADDRESS().html

---

Safety address: Upper value # 20616.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCSAFETYUPPERBOUNDADDRESS {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLCSAFETYUPPERBOUNDADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Safety address (upper value) at safety modules. Detailed information on this is available from the PLC manufacturer. The value is filled during the import of PLC configuration data in the AutomationML AR APC format. The properties for the safety addresses are taken into consideration for the PLC data exchange as of AutomationML AR APC Version 1.1.0.
