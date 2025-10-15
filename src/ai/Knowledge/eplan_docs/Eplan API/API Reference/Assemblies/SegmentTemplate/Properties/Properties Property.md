# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate~Properties.html

---

EPLAN properties of the SegmentTemplate object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new SegmentTemplatePropertyList Properties {get;}
```
```

```
```
public:

new property SegmentTemplatePropertyList^ Properties {

   SegmentTemplatePropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-216a1a12-68b8-4701-ad81-e3b258a6b1a4)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
