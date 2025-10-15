# ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1687.html

---

Suitable for degree of protection (IP) # 26358.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP {get; set;}
```
```

```
```
public:

property MDPropertyValue^ ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Classification of the protection of a device or a component against the penetration of foreign objects and water. The IP degree of protection (International Protection) is specified by two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
