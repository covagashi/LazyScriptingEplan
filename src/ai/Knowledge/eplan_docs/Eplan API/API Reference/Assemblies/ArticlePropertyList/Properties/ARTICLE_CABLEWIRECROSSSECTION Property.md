# ARTICLE_CABLEWIRECROSSSECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEWIRECROSSSECTION().html

---

Connection: Cross-section / diameter # 22032.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_CABLEWIRECROSSSECTION {get; set;}
```
```

```
```
public:

property PropertyValue^ ARTICLE_CABLEWIRECROSSSECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Connection cross-section / diameter of the cable connection of a cable. For pipes and hoses in fluid power and process engineering the property refers to the inner diameter. A corresponding property "Outside diameter" exists for the outside diameter.
