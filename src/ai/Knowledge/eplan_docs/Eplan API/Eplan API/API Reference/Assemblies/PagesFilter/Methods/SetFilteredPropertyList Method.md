# SetFilteredPropertyList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~SetFilteredPropertyList.html

---

Sets the [PagePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html) that [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching the filter must have.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetFilteredPropertyList( 
   PagePropertyList searchedPropList
)
```
```

```
```
public:
void SetFilteredPropertyList( 
   PagePropertyList^ searchedPropList
)
```
```

#### Parameters

*searchedPropList*
:   List of the P8 properties the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |



See Also

#### Reference

[PagesFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter.html)
  
[PagesFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter_members.html)