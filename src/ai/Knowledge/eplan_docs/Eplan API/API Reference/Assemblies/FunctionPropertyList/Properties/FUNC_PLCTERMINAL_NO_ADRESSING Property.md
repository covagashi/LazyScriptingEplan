# FUNC_PLCTERMINAL_NO_ADRESSING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCTERMINAL_NO_ADRESSING().html

---

Do not include in addressing # 20380.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCTERMINAL_NO_ADRESSING {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLCTERMINAL_NO_ADRESSING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, the PLC connection point is excluded from addressing and retains its original address. Fixed hardware addresses are thus not changed during subsequent addressing or during the insertion of macros.
