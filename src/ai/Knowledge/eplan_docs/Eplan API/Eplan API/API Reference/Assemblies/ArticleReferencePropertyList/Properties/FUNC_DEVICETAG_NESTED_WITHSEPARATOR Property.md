# FUNC_DEVICETAG_NESTED_WITHSEPARATOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_NESTED_WITHSEPARATOR().html

---

DT (subordinate, without project structures, with preceding sign) # 20212.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_DEVICETAG_NESTED_WITHSEPARATOR {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_DEVICETAG_NESTED_WITHSEPARATOR {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the subordinate device tag without the project structures, but with information about the preceding sign.

Example: "-K1" is output for "=A+O-U1-K1".



See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_NESTED_WITHSEPARATOR.html)