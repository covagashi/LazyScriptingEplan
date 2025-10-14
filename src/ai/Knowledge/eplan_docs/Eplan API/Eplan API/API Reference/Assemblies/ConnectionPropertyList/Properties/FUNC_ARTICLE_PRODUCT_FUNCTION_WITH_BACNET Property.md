# FUNC_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic170.html

---

BACnet: Product function # 26539.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET {
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

The product function describes the specific tasks and capabilities of a product within a BACnet network, e.g. temperature control, light control, etc.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET.html)