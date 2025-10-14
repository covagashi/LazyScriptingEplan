# Articles Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Articles.html

---

Returns [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s that are referenced by Connection, and only those that are stored in project database.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual Article[] Articles {get;}
```
```

```
```
public:
virtual property array<Article^>^ Articles {
   array<Article^>^ get();
}
```
```

#### Property Value

Articles related with the Function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for connections throws exception |



See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)
  
[Article Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)