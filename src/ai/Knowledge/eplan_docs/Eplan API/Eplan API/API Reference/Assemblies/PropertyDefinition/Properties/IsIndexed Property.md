# IsIndexed Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsIndexed.html

---

Allows to check if a given property is indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsIndexed {get;}
```
```

```
```
public:
property bool IsIndexed {
   bool get();
}
```
```

#### Property Value

â¢ true = Property is indexed

â¢ false = Property is not indexed

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when called for PropertyDefinition created as a conversion from other type. |

Remarks

Can only be called after retrieving a property list from the given API class.

Example

- [C#](#i-tab-content-fbc1c158-4dea-4ed0-a598-cd04d2bd7206)

```

Article article = myProject.Articles[0]; // A valid Article object

bool isIndexed = article.Properties.ARTICLE_HEIGHT.Definition.IsIndexed;


```

See Also

#### Reference

[PropertyDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)
  
[PropertyDefinition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition_members.html)