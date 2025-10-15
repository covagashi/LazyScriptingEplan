# FUNC_ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic592.html

---

Suitable for cable diameter # 26351.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Possible cable diameters for which a specific product or component is suitable.
