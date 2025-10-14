# FUNC_ARTICLE_WEIGHT_OF_THE_INDIVIDUAL_ARTICLE_PACKAGING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic604.html

---

Weight (individual packaging) # 26377.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_WEIGHT_OF_THE_INDIVIDUAL_ARTICLE_PACKAGING( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_WEIGHT_OF_THE_INDIVIDUAL_ARTICLE_PACKAGING {
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

Weight of the individual part packaging. Weight of the primary packaging that is directly around the individual product, without additional protective packaging.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2042.html)