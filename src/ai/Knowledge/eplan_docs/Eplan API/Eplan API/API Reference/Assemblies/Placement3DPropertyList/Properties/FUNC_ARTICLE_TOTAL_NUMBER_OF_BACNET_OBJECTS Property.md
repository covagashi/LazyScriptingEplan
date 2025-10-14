# FUNC_ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic596.html

---

BACnet: Total number of objects # 26211.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of all objects or object types in the BACnet protocol.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2036.html)