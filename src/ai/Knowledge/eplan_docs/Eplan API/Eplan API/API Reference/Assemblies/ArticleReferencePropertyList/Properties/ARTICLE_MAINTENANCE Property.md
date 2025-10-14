# ARTICLE_MAINTENANCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_MAINTENANCE().html

---

Lubrication / maintenance # 22141.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_MAINTENANCE {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_MAINTENANCE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Lubrication / maintenance information, e.g. the maintenance interval.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.



See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_MAINTENANCE.html)