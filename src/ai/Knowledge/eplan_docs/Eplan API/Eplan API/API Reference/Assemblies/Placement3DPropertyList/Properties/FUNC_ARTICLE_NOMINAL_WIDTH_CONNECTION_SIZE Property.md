# FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic559.html

---

Nominal size / connection size # 26515.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE {
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

Nominal specification for the diameter of the process connection point, e.g. DN 25. The nominal size is a numerical size designation that is used for the items for which the outside diameter or thread size is not specified. Describes the size of connection points and connections in piping systems with regard to the connection compatibility of components such as pipes or fittings.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE.html)