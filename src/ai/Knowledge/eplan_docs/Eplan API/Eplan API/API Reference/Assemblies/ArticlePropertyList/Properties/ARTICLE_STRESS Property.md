# ARTICLE_STRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STRESS().html

---

Stress # 22143.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_STRESS {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_STRESS {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

The types of stress differentiate between mechanical movement values (static and dynamic) and environmental influences (e.g., moisture, heat, chemical reactions).

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.



See Also

#### Reference

[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[ArticlePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_STRESS.html)