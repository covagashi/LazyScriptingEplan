# ArticleReferences Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~ArticleReferences.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Function.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override ArticleReference[] ArticleReferences {get;}
```
```

```
```
public:
property array<ArticleReference^>^ ArticleReferences {
   array<ArticleReference^>^ get() override;
}
```
```

#### Property Value

ArticleReferences related with the Function.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for Functions throws exception |

Remarks

The property does not work for Functions retrieved from transient objects, like macros. In this case please use properties FUNC\_ARTICLE\_PARTNR, FUNC\_ARTICLE\_VARIANT, FUNC\_ARTICLE\_COUNT



See Also

#### Reference

[ConnectionDefinitionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)
  
[ConnectionDefinitionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint_members.html)
  
[ArticleReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)