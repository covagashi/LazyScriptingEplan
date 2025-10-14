# FUNC_ARTICLE_POWER_REQUIREMENT_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MAX(Int32).html

---

Power requirement, max. # 26422.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_POWER_REQUIREMENT_MAX( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_POWER_REQUIREMENT_MAX {
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

Maximum quantity of energy that a device or plant requires to function properly. The power requirement describes the theoretical maximum power requirement.



See Also

#### Reference

[ProjectPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html)
  
[ProjectPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_REQUIREMENT_MAX.html)