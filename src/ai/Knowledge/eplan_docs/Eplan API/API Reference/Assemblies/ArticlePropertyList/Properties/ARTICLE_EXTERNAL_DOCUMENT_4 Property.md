# ARTICLE_EXTERNAL_DOCUMENT_4 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EXTERNAL_DOCUMENT_4().html

---

External document 4 # 22235.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_EXTERNAL_DOCUMENT_4 {get; set;}
```
```

```
```
public:

property PropertyValue^ ARTICLE_EXTERNAL_DOCUMENT_4 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

The "External document [n]" properties always show the nth external document assigned to the part. For example "External document 1" shows the first external document assigned to the part.
