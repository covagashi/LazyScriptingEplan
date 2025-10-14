# FUNC_DEVICETAG_FULLNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_FULLNAME().html

---

Name (without project structures) # 20058.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_DEVICETAG_FULLNAME {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_DEVICETAG_FULLNAME {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Specifies the full name of a function without the project structures.

Example: "U1-X1" is output for a terminal strip "=A+O-U1-X1" and "X2:3" is output for a terminal "=A-X2:3".



See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_FULLNAME.html)