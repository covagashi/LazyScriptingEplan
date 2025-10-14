# AddArticleReference(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~AddArticleReference(String).html

---

Adds a new [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the IArticleUser. Returns the added [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
ArticleReference AddArticleReference( 
   string strArticleNR
)
```
```

```
```
ArticleReference^ AddArticleReference( 
   String^ strArticleNR
)
```
```

#### Parameters

*strArticleNR*
:   number of added article

#### Return Value

ArticleReference added to the IArticleUser

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when this IArticleUser cannot have Articles |
| [System.ArgumentNullException](#) | Thrown when `strArticleName` is `null`. |

Remarks

Stores the article from System article database in the Project Adds one article with variant 1 and count 1



See Also

#### Reference

[IArticleUser Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser.html)
  
[IArticleUser Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~AddArticleReference.html)
  
[ArticleReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)