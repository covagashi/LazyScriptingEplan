# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Properties.html

---

Represents ArticleReference properties

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new ArticleReferencePropertyList Properties {get;}
```
```

```
```
public:

new property ArticleReferencePropertyList^ Properties {

   ArticleReferencePropertyList^ get();

}
```
```

Remarks

Properties from `ArticleReferencePropertyList` have another ids than these from parent object or in the 'Part reference data' tab in GUI. In order to use the same ids as in GUI, please use parent object ids (see the first example). When accessing user-defined property by a parent object, there is necessary to add 'EPLAN.ArticleRef.' prefix to its identifying name. Also there must by the index provided which is position of an ArticleReference at a parent object.

Example

Setting article reference properties by parent object ids Setting article reference properties by ArticleReferencePropertyList ids Getting article reference user-defined property by parent object

- [C#](#i-tab-content-862befdb-de9b-4a04-b35b-1e66bd26c9ad)

```
articleReference.ParentObject.Properties[Properties.Function.FUNC_ARTICLE_NOTE, 1] = "ARTICLE_NOTE3";

string note = articleReference.ParentObject.Properties[Properties.Function.FUNC_ARTICLE_NOTE, 1];
```

- [C#](#i-tab-content-c0800149-62d0-4856-b8b9-3296f9f4a997)

```
articleReference.Properties[Properties.ArticleReference.ARTICLE_NOTE] = "note";

string note = articleReference.Properties[Properties.ArticleReference.ARTICLE_NOTE];
```

- [C#](#i-tab-content-9f3bca8a-a649-4722-93d3-7f8f857a5fcc)

```
var propertyValue = project.Properties["EPLAN.ArticleRef.UserProperty.1"][1].ToString();
```
