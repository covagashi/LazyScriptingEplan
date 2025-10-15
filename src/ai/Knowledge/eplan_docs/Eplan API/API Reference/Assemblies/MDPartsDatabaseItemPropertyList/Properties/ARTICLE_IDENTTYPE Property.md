# ARTICLE_IDENTTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_IDENTTYPE().html

---

Barcode type # 22209.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_IDENTTYPE {get; set;}
```
```

```
```
public:

property MDPropertyValue^ ARTICLE_IDENTTYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Shows the type of coding for a barcode, e.g. 2D code, EAN/GTIN, ISBN etc. The contents of this property can be taken into account in manufacturing lists and when importing and exporting parts; it cannot be translated.
