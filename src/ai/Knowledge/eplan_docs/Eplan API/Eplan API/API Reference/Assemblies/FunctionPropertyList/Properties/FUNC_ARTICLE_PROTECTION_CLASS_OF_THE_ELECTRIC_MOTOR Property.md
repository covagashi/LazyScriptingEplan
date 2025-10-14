# FUNC_ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic235.html

---

Protection type class (motor) # 26566.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR {
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

Classifies the extent of protection of an electric motor against direct contact, against penetration of solid foreign objects and/or against penetration of water. This degree of protection is indicated by the IP code (International Protection), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.



See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](topic1860.html)