# FUNC_ARTICLE_TORQUE_AT_MIN_SPEED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_AT_MIN_SPEED(Int32).html

---

Torque (at min. rotation speed) # 26252.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_TORQUE_AT_MIN_SPEED( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_TORQUE_AT_MIN_SPEED {
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

Torque at the minimum permissible output speed of the drive engine.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_TORQUE_AT_MIN_SPEED.html)