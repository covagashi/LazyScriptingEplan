# FUNC_PLUGCODING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLUGCODING().html

---

Plugs: Coding # 20856.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLUGCODING {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_PLUGCODING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Coding is useful in order to distinguish between several plugs. By default, the property is preset with the value of the part property (ID 22103) of the same name of the associated part.
