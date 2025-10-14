# FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic522.html

---

Actual power (hydraulic) # 26382.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC {
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

Hydraulic power output or consumption (product of rated flow rate and pressure of a pressure fluid) of the component or system determined at the time under consideration.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC.html)