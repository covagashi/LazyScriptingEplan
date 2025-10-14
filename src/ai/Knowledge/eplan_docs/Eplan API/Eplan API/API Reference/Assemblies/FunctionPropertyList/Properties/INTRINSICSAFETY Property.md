# INTRINSICSAFETY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~INTRINSICSAFETY().html

---

Intrinsically safe # 31030.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue INTRINSICSAFETY {get; set;}
```
```

```
```
public:
property PropertyValue^ INTRINSICSAFETY {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

Functions, connections, and connection definition points are defined as intrinsically safe using this property. The intrinsic safety at the function forces intrinsic safety at the associated connection points for which intrinsic safety is possible.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~INTRINSICSAFETY.html)