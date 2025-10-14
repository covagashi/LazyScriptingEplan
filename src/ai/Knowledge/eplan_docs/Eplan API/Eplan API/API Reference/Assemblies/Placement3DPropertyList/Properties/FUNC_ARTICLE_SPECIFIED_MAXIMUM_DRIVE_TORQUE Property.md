# FUNC_ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic588.html

---

Drive torque (specified), max. # 26571.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Permissible maximum drive torque for which an item or system is designed.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2032.html)