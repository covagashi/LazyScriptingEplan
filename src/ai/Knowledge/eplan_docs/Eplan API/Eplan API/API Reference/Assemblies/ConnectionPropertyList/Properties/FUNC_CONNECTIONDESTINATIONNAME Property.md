# FUNC_CONNECTIONDESTINATIONNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CONNECTIONDESTINATIONNAME(Int32).html

---

Name of target connection point # 20077.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CONNECTIONDESTINATIONNAME( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_CONNECTIONDESTINATIONNAME {
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

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Provides the name of a target connection point. This consists of the connection point designation. For terminals and pins, the terminal or pin designation is output in addition to the connection point designation.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_CONNECTIONDESTINATIONNAME.html)