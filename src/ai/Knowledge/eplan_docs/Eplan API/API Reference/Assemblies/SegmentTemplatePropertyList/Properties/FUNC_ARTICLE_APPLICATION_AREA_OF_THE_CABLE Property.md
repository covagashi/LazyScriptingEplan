# FUNC_ARTICLE_APPLICATION_AREA_OF_THE_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1110.html

---

Connecting cable: Application area # 26209.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_APPLICATION_RANGE_OF_THE_CONNECTION_CABLE( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_APPLICATION_RANGE_OF_THE_CONNECTION_CABLE {

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

Type of usage of the connection cable.
