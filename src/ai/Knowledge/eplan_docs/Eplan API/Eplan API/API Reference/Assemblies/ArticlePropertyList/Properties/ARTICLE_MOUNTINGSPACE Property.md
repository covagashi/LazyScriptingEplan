# ARTICLE_MOUNTINGSPACE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MOUNTINGSPACE().html

---

Space requirement # 22047.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_MOUNTINGSPACE {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_MOUNTINGSPACE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Double.

Remarks

Specify the space requirement of the part here. If values are entered for the properties Width and Height, the space requirement is determined automatically in accordance with the following formula: (w\*h) with w = Width and h = Height.



See Also

#### Reference

[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[ArticlePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MOUNTINGSPACE.html)