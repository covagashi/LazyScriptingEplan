# FUNC_FIXED_DEVICE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_FIXED_DEVICE().html

---

Device protection # 20475.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_FIXED_DEVICE {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_FIXED_DEVICE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Specifies whether a device protection is assigned to the function, connection or planning object. The assigned parts cannot be changed at a device / planning object with device protection. All the properties that are assigned through the part (and the function templates stored at the part) are thus protected.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_FIXED_DEVICE.html)