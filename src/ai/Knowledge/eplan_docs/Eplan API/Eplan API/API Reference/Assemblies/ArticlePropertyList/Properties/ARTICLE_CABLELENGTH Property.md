# ARTICLE_CABLELENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLELENGTH().html

---

Length (prefabricated) # 22055.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_CABLELENGTH {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_CABLELENGTH {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Double.

Remarks

Property of a part variant. Length of cables, bundles, pipes, tubes and wires is stored internally in the unit "meter" and is converted to the unit selected for the display. What is meant here is the "unchangeable" length with which a part is to be used, not the delivery length.



See Also

#### Reference

[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[ArticlePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLELENGTH.html)