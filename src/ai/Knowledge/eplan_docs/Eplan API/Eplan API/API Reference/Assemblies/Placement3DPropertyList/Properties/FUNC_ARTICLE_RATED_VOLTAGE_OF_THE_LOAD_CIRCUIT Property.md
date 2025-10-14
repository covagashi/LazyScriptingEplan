# FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_LOAD_CIRCUIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic585.html

---

Nominal voltage (load circuit) # 26495.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_LOAD_CIRCUIT( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_LOAD_CIRCUIT {
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

Specified voltage in volt, which is foreseen for the operation of an electrical load circuit.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2030.html)