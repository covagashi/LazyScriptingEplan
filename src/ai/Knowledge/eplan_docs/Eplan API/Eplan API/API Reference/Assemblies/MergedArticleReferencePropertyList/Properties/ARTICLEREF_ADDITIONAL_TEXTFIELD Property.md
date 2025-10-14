# ARTICLEREF_ADDITIONAL_TEXTFIELD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_ADDITIONAL_TEXTFIELD().html

---

Suppl. field: Text # 20501.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLEREF_ADDITIONAL_TEXTFIELD {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLEREF_ADDITIONAL_TEXTFIELD {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Supplementary field for part reference data. Serves for the entry of free additional properties. Outputs the value of the "Supplementary field text" (ID 20915) per part reference. You have to note the meaning specified by you of the supplementary field. This property can be used, for example in block properties or as a filter criterion in reports and during the manufacturing data export.



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_ADDITIONAL_TEXTFIELD.html)