# FUNC_CABLEWIRECOUNTANDCROSSSECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLEWIRECOUNTANDCROSSSECTION().html

---

Cable / Conduit: Number of connections and cross-section / diameter # 20053.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CABLEWIRECOUNTANDCROSSSECTION {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_CABLEWIRECOUNTANDCROSSSECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Displays the number of connections multiplied by the cross-section (or diameter), separated by "x".
