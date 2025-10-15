# DESIGNATION_SUBFUNCTIONALASSIGNMENT4_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic797.html

---

Functional assignment (sub-identifier 5) # 1305.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DESIGNATION_SUBFUNCTIONALASSIGNMENT5 {get; set;}
```
```

```
```
public:

property PropertyValue^ DESIGNATION_SUBFUNCTIONALASSIGNMENT5 {

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
