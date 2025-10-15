# ARTICLE_WIDTHRATING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_WIDTHRATING().html

---

Nominal size # 22225.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_WIDTHRATING {get; set;}
```
```

```
```
public:

property MDPropertyValue^ ARTICLE_WIDTHRATING {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property should no longer be used and is only available with earlier Eplan versions for reasons of compatibility. In older Eplan projects (created with version 2.2 or earlier), this property was used to assign the diameter of a pipe / hose line or the size / connection dimension of a control valve (valve, slide) to a part variant. Together with the nominal pressure level, the nominal width defines all dimensions of a pipe. The designation DN ("diameter nominal") is used to specify the nominal width, followed by a number without a unit that is roughly equivalent to the inner diameter in millimeters.
