# FUNCTION3D_ELEM_ISFIXONPARENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ELEM_ISFIXONPARENT().html

---

Item is immovably attached to the superior item # 36010.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_ELEM_ISFIXONPARENT {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_ELEM_ISFIXONPARENT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is enabled, then the item cannot be moved relative to the superior item. Moving the entire mounting panel by means of the "Move" functionality is still possible. The fixation can be temporarily revoked for individual items by pressing the [Shift] key while moving via Drag & Drop.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ELEM_ISFIXONPARENT.html)