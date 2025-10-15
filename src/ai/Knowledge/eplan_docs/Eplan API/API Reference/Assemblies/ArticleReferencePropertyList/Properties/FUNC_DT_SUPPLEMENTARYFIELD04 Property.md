# FUNC_DT_SUPPLEMENTARYFIELD04 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DT_SUPPLEMENTARYFIELD04().html

---

DT: Supplementary field 4 # 20159.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_DT_SUPPLEMENTARYFIELD04 {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_DT_SUPPLEMENTARYFIELD04 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Can be used in the DT. This property is available only in certain, customer-specific Eplan versions, and can be used if you have selected the "Edit DT in individual fields" project setting.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
