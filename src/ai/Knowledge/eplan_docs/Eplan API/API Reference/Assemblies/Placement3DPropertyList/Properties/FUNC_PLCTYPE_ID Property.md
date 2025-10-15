# FUNC_PLCTYPE_ID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCTYPE_ID().html

---

PLC type designation # 20416.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCTYPE_ID {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLCTYPE_ID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

PLC type designation of a PLC card. The part allocation during the import of PLC configuration files is carried out on the basis of this property (in as far as no device description file is specified). The entry has to be carried out in exactly the same notation as in the hardware catalog of the manufacturer. In the simplest case the PLC type designation corresponds to the order number. During a part selection or device selection the property is filled with the corresponding value from the parts management.
