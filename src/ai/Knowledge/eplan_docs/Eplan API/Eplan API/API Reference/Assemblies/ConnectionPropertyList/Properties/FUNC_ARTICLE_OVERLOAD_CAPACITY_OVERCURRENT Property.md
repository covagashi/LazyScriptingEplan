# FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic165.html

---

Overload capability: Overcurrent # 26620.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT {
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

Ability to assimilate an overcurrent briefly - as a result of a current consumption exceeding the nominal current.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT.html)