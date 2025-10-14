# AddArticleReference(String,String,UInt32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~AddArticleReference(String,String,UInt32).html

---

Adds a new [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) to the Function3D. Returns the added [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual ArticleReference AddArticleReference( 
   string strArticleNR,
   string strVariantNR,
   uint nCount
)
```
```

```
```
public:
virtual ArticleReference^ AddArticleReference( 
   String^ strArticleNR,
   String^ strVariantNR,
   uint nCount
)
```
```

#### Parameters

*strArticleNR*
:   article's number

*strVariantNR*
:   article's variant number

*nCount*
:   count of articles to add

#### Return Value

Article added to the Function3D

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Article cannot be added |
| [System.ArgumentNullException](#) | Thrown when `strArticleNR` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariantNR` is `null`. |
| [Eplan.EplApi.DataModel.CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | Thrown when it was impossible to get valid `property index`. |
| [Eplan.EplApi.DataModel.CannotAddArticleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.CannotAddArticleException.html) | When 2nd ArticleReference is added to a Function3D having ArticlePlacement category |

Remarks

Stores the article from System article database in the Project. Functions3D of category ArticlePlacement can have only 1 ArticleReference object.



See Also

#### Reference

[Function3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)
  
[Function3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~AddArticleReference.html)
  
[ArticleReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)