# IsReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsReadOnly.html

---

Allows to check if a given property is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsReadOnly {get;}
```
```

```
```
public:
property bool IsReadOnly {
   bool get();
}
```
```

#### Property Value

â¢ true = Property is read-only

â¢ false = Property is not read-only

Remarks

Can only be called after retrieving a property list from the given API class.

Example

- [C#](#i-tab-content-5e047ce5-43e2-4606-862e-eebf21ea169f)

```

Article article = myProject.Articles[0]; // A valid Article object

bool isReadOnly = article.Properties.ARTICLE_HEIGHT.Definition.IsReadOnly;


```

See Also

#### Reference

[PropertyDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)
  
[PropertyDefinition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition_members.html)