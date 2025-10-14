# FUNC_ARTICLE_MAINTENANCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAINTENANCE(Int32).html

---

Lubrication / maintenance # 20912.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_MAINTENANCE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_MAINTENANCE {
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

Lubrication / maintenance information, e.g. the maintenance interval. A max. of 50 definitions can be defined using the index.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_MAINTENANCE.html)