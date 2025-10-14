# ArticleModules Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleModules.html

---

Returns an array of [Article.Module](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article+Module.html) objects representing module items. Array contains a lists of subparts structured by device tag (DT).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Article.Module[] ArticleModules {get;}
```
```

```
```
public:
property array<Article.Module^>^ ArticleModules {
   array<Article.Module^>^ get();
}
```
```

Remarks

This property makes sense only for article that is a module. If this article is not a module or it doesn't contain any module subparts, an empty array is returned.



See Also

#### Reference

[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)
  
[Article Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article_members.html)