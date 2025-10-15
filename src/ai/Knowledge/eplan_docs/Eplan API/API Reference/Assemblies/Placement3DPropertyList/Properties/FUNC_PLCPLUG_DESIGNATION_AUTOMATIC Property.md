# FUNC_PLCPLUG_DESIGNATION_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCPLUG_DESIGNATION_AUTOMATIC().html

---

Plug designation (automatic) # 20431.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCPLUG_DESIGNATION_AUTOMATIC {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLCPLUG_DESIGNATION_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Plug designation automatically determined for PLC connection points / channels and device connection points. The plug designation supports the identification of PLC connection points or device connection points.
