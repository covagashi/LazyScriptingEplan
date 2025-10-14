# ARTICLE_ERPNR_8 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR_8().html

---

ERP / PDM number 8 # 22377.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_ERPNR_8 {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_ERPNR_8 {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Unique part number of an external ERP system or PDM system. The ERP / PDM numbers must be unique for different parts. Same values are also permitted for the properties "ERP / PDM number 1" to "ERP / PDM number 10" at a part. Any number of characters can be entered for the ERP / PDM number. However, only the first 64 characters in UTF-8 format are identifying. If you assign a value via the Application Programming Interface you have to specify the same value for all part variants.



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR_8.html)