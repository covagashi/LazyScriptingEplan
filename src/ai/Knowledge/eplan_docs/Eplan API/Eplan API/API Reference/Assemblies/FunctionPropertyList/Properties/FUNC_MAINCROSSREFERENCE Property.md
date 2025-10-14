# FUNC_MAINCROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MAINCROSSREFERENCE().html

---

Cross-reference (only main functions) # 20306.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_MAINCROSSREFERENCE {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_MAINCROSSREFERENCE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows cross-references for possible main functions of the device. The function category has to match here. This property can be used to show a cross-reference on a black box to the same black box placed elsewhere.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MAINCROSSREFERENCE.html)