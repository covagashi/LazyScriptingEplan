# GetPagesWithCF Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPagesWithCF.html

---

Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Page[] GetPagesWithCF( 
   ICustomFilter filter
)
```
```

```
```
public:
array<Page^>^ GetPagesWithCF( 
   ICustomFilter^ filter
)
```
```

#### Parameters

*filter*
:   a custom filter object implementing [ICustomFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)

#### Return Value

\* [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given custom filter. \* All [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |



See Also

#### Reference

[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[DMObjectsFinder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder_members.html)
  
[ICustomFilter Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter.html)