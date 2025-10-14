# FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic580.html

---

Transport capacity of the operating fluid # 26327.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID {
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

Volume of the operating fluid that flows through the device per unit of time.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2028.html)