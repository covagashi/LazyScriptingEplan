# FUNC_TERMINAL_PLCADDRESS_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINAL_PLCADDRESS_AUTOMATIC().html

---

Connected PLC address (automatic) # 20855.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_TERMINAL_PLCADDRESS_AUTOMATIC {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_TERMINAL_PLCADDRESS_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

PLC address of a connected PLC connection point for pins and terminals (can be automatically determined over several terminals/pins).
