# IsPropertyLicensed Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsPropertyLicensed.html

---

Allows to check if a given property is licensed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsPropertyLicensed {get;}
```
```

```
```
public:

property bool IsPropertyLicensed {

   bool get();

}
```
```

#### Property Value

â¢ true = Property is licensed

â¢ false = Property is not licensed

Remarks

Can only be called after retrieving a property list from the given API class.

Example

- [C#](#i-tab-content-5b395ea9-8a73-4aa1-82e5-588c360fa0fb)

```


Article article = myProject.Articles[0]; // A valid Article object



bool isPropertyLicensed = article.Properties.ARTICLE_HEIGHT.Definition.IsPropertyLicensed;





```
