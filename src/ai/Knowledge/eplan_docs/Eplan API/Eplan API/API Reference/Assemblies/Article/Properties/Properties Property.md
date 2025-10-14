# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~Properties.html

---

.NET Property enabling access to P8 properties of the Article object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new ArticlePropertyList Properties {get;}
```
```

```
```
public:
new property ArticlePropertyList^ Properties {
   ArticlePropertyList^ get();
}
```
```

#### Property Value

P8 properties of the Article.

Example

- [C#](#i-tab-content-3f7d186e-35bb-44df-a720-8daef22d646c)

```
Article a;//a valid Article
a.Properties[Properties.Article.ARTICLE_NOTE] = "note";
string s = a.Properties[Properties.Article.ARTICLE_SUPPLIER];
```

See Also

#### Reference

[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)
  
[Article Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article_members.html)
  
[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)