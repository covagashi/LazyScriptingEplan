# FUNC_MAXCROSSREFERENCEBLOCKCOUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_MAXCROSSREFERENCEBLOCKCOUNT().html

---

Cross-reference display: Max. number of cross-references # 20198.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_MAXCROSSREFERENCEBLOCKCOUNT {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_MAXCROSSREFERENCEBLOCKCOUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the maximum number of cross-references that can be shown for a function or interruption point. The value "0" does not relate to any limitation of the cross-reference display.
