# ToString(Language,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToString(Language,String).html

---

Returns string value of this property. When type of property is MultiLangString then only specified language is returned. In case of offline MDPropertyValue object, stored value is returned without any cast. When property can not be read, `default_value` is returned instead of throwing `MDEmptyPropertyException` .

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string ToString( 

   ISOCode.Language language,

   string default_value

)
```
```

```
```
public:

String^ ToString( 

   ISOCode.Language language,

   String^ default_value

)
```
```

#### Parameters

*language*
:   Language to extract from MultiLangString value.

*default\_value*
:   Default value which is retuned when property cannot be read.

#### Return Value

Value of string or `default_value` when property can not be read from object or properties list.
