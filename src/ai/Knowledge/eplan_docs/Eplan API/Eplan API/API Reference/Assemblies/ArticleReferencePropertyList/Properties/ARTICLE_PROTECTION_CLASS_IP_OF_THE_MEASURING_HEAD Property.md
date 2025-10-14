# ARTICLE_PROTECTION_CLASS_IP_OF_THE_MEASURING_HEAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic62.html

---

Degree of protection (IP): Measuring head # 26557.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_PROTECTION_CLASS_IP_OF_THE_MEASURING_HEAD {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_PROTECTION_CLASS_IP_OF_THE_MEASURING_HEAD {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Describes the degree of protection offered by the housing of the measurement head against the penetration of foreign objects (such as dust) and water. These protection categories are indicated by the IP code (International Protection Code), which consists of two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.



See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](topic1770.html)