# ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic320.html

---

Protection type class (motor) # 26565.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Classifies the extent of protection of an electric motor against direct contact, against penetration of solid foreign objects and/or against penetration of water. This degree of protection is indicated by the IP code (International Protection), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](topic1906.html)