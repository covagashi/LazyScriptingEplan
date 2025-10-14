# ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic283.html

---

Power circuit breaker - test available # 26433.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specifies whether a power circuit breaker has already been checked and the corresponding check results are available. Example: For a low-voltage power circuit breaker the check includes, for example, the check of the contact resistance, the switching time measurement and the isolation test.



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](topic1879.html)