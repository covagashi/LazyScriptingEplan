# ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic314.html

---

Performance description, standardized: Performance group item number # 26431.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Unique identification number for a specific service item within a service group in the bill of quantities. Each service group contains several service items that can be identified by such a unique number. Example: In a performance group "Piping and support systems" a specific number stands for the position "Drilling through walls and ceilings made of masonry".



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](topic1901.html)