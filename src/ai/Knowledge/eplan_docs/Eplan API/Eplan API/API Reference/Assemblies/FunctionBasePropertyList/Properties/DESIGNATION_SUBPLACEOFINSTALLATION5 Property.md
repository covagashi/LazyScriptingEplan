# DESIGNATION_SUBPLACEOFINSTALLATION5 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~DESIGNATION_SUBPLACEOFINSTALLATION5().html

---

Installation site (sub-identifier 5) # 1405.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DESIGNATION_SUBPLACEOFINSTALLATION5 {get; set;}
```
```

```
```
public:
property PropertyValue^ DESIGNATION_SUBPLACEOFINSTALLATION5 {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.



See Also

#### Reference

[FunctionBasePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html)
  
[FunctionBasePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~DESIGNATION_SUBPLACEOFINSTALLATION5.html)