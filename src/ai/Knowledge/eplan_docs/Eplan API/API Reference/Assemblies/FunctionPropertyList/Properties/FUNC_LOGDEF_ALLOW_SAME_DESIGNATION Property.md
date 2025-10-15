# FUNC_LOGDEF_ALLOW_SAME_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_LOGDEF_ALLOW_SAME_DESIGNATION(Int32).html

---

Connection point logic: Allow identical connection point designation # 20372.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_LOGDEF_ALLOW_SAME_DESIGNATION( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_LOGDEF_ALLOW_SAME_DESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
