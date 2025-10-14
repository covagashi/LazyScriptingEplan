# FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic595.html

---

Temperature range (medium), min. # 26618.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN {
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

Minimum temperature range that a medium (such as a liquid or a gas) can reach while flowing through a device or component without causing damage or impairing its functionality.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN.html)