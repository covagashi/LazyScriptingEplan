# FUNC_CROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList~FUNC_CROSSREFERENCE().html

---

Cross-reference (main / aux. function) # 20300.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CROSSREFERENCE {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_CROSSREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows cross-references between main and auxiliary functions. Cross-references between structure boxes are not shown here.
