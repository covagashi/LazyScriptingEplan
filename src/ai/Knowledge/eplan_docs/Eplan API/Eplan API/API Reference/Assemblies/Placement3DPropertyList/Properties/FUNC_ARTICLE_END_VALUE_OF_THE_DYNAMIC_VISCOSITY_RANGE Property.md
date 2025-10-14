# FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic540.html

---

Dynamic viscosity range: End value # 26300.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE {
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

Highest value of the dynamic viscosity specified for a particular product or material. The dynamic viscosity is a measure of the viscosity of a fluid and is measured in pascal seconds (PaÂ·s).



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2012.html)