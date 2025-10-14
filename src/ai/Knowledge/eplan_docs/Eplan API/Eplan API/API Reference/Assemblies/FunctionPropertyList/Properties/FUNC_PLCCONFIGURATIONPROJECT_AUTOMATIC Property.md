# FUNC_PLCCONFIGURATIONPROJECT_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCONFIGURATIONPROJECT_AUTOMATIC().html

---

Configuration project (automatic, at bus ports) # 20581.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCCONFIGURATIONPROJECT_AUTOMATIC {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCCONFIGURATIONPROJECT_AUTOMATIC {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the manually entered configuration project at a bus port or, if it is empty, the configuration project of the associated PLC box (main function).



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCONFIGURATIONPROJECT_AUTOMATIC.html)