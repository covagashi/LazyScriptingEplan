# Equals(PropertyValue) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Equals(PropertyValue).html

---

Determines whether two PropertyValues objects have the same value.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool Equals( 

   PropertyValue other

)
```
```

```
```
public:

bool Equals( 

   PropertyValue^ other

)
```
```

#### Parameters

*other*

#### Return Value

True when both values are the same.

Remarks

If member IsEmpty of compared property value is true then an empty string is used as a value for comparison.
