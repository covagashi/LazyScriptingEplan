# RemoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~RemoveArticleReference.html

---

Removes the ArticleReference from the IArticleUser

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void RemoveArticleReference( 
   ArticleReference artRef
)
```
```

```
```
void RemoveArticleReference( 
   ArticleReference^ artRef
)
```
```

#### Parameters

*artRef*
:   The articlereference to remove

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `artRef` is `null`. |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object in the articlereference is not this IArticleUser |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if Eplan.EplApi.DataModel.Function.IsFixedDevice is true. |

Remarks

The articlereference must belong to the IArticleUser.



See Also

#### Reference

[IArticleUser Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser.html)
  
[IArticleUser Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser_members.html)
  
[ArticleReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)