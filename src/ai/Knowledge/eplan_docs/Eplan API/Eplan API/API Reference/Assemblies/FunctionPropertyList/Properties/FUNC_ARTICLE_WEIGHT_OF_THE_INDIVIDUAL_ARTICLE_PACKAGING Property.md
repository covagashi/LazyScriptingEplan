# FUNC_ARTICLE_WEIGHT_OF_THE_INDIVIDUAL_ARTICLE_PACKAGING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic250.html

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

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](topic1867.html)