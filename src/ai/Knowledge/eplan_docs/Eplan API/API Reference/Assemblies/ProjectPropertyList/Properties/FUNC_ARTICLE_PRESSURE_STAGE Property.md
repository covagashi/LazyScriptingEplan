# FUNC_ARTICLE_PRESSURE_STAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PRESSURE_STAGE(Int32).html

---

Pressure level # 26260.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_PRESSURE_STAGE( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_PRESSURE_STAGE {

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

Maximum pressure load that an item or material can withstand without being damaged. This specification is important for components that are operated in pressure systems or under high pressure, such as pipes, valves or pressure vessels. The pressure level is usually expressed in bar or pascal (Pa).
