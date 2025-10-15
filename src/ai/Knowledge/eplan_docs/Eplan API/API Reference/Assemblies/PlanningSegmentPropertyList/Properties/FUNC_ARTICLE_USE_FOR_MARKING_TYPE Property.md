# FUNC_ARTICLE_USE_FOR_MARKING_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1055.html

---

Safety-related values: Use case in use # 20307.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_USED_SAFETYRELATEDVALUE( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_USED_SAFETYRELATEDVALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Indicates the use case that is used for the safety-related values of a part.
