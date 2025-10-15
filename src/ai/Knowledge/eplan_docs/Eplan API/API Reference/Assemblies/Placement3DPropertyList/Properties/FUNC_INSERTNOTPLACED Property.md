# FUNC_INSERTNOTPLACED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_INSERTNOTPLACED().html

---

Insert from macro as unplaced # 20094.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_INSERTNOTPLACED {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_INSERTNOTPLACED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

For functions saved in macros. If this property is assigned to a function, the function is not placed in the schematic when the macro is placed. The function is then only available as an unplaced function in the project.
