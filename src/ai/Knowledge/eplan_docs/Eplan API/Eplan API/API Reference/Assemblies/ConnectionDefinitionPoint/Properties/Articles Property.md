# Articles Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~Articles.html

---

Returns [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Function, and only those that are stored in project database.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override Article[] Articles {get;}
```
```

```
```
public:
property array<Article^>^ Articles {
   array<Article^>^ get() override;
}
```
```

#### Property Value

Articles related with the Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for connections throws exception |

Remarks

This function returns only articles which are stored in the project. Although function might contain reference to Article (which resists in system database), so in this case following Properties need to be used: FUNC\_ARTICLE\_PARTNR, FUNC\_ARTICLE\_VARIANT, FUNC\_ARTICLE\_COUNT etc.



See Also

#### Reference

[ConnectionDefinitionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)
  
[ConnectionDefinitionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint_members.html)
  
[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)