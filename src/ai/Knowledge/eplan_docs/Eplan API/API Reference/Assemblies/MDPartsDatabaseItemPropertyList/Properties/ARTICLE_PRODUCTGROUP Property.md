# ARTICLE_PRODUCTGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PRODUCTGROUP().html

---

Product group # 22041.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_PRODUCTGROUP {get; set;}
```
```

```
```
public:

property MDPropertyValue^ ARTICLE_PRODUCTGROUP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Outputs the product group entered in parts management on the "Properties" tab > hierarchy level "General" > "Product grouping" property. The parts are sorted according to their product groups (including superseding and subgroups) and displayed in tree format in parts management.
