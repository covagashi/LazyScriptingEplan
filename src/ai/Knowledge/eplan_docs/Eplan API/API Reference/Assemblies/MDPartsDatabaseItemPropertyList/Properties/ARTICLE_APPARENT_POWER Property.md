# ARTICLE_APPARENT_POWER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_APPARENT_POWER().html

---

Apparent power # 26549.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_APPARENT_POWER {get; set;}
```
```

```
```
public:

property MDPropertyValue^ ARTICLE_APPARENT_POWER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Total power available in an AC circuit. It is composed of the active power and the reactive power. The apparent power is measured in volt amperes (VA) and is obtained as the product of the root mean square value of the electric voltage and the root mean square value of the electric amperage.
