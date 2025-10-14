# FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD08 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic642.html

---

Supplementary field 8 # 20147.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD08( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_SUPPLEMENTARYFIELD08 {
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

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Using the index, you can differentiate between up to 10 supplementary fields.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2066.html)