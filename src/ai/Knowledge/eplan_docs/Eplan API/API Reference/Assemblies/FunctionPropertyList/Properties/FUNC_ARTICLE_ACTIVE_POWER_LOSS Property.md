# FUNC_ARTICLE_ACTIVE_POWER_LOSS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_LOSS(Int32).html

---

Active power loss # 26622.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_ACTIVE_POWER_LOSS( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ FUNC_ARTICLE_ACTIVE_POWER_LOSS {

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

Electrical power that is lost in a device or system in the form of heat or other losses, for example because materials are remagnetized and/or heated. This power is measured in watt (W) and indicates how much energy is not converted into usable work.
