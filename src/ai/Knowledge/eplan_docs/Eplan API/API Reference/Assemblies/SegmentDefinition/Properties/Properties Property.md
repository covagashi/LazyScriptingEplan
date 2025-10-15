# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~Properties.html

---

EPLAN properties of the SegmentDefinition object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new SegmentDefinitionPropertyList Properties {get;}
```
```

```
```
public:

new property SegmentDefinitionPropertyList^ Properties {

   SegmentDefinitionPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-7d3f2385-8f95-4ae2-b9ed-3671b1d7675d)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
