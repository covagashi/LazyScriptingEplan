# FUNC_ARTICLE_TEMPERATURE_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1045.html

---

Temperature, min. # 26614.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_TEMPERATURE_MIN( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_TEMPERATURE_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum operating temperature that a device or component can withstand safely without being damaged or functionality being impaired.
