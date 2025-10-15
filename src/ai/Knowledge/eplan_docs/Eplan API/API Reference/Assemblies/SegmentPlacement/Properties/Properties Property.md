# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~Properties.html

---

EPLAN properties of the SegmentPlacement object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new SegmentPlacementPropertyList Properties {get;}
```
```

```
```
public:

new property SegmentPlacementPropertyList^ Properties {

   SegmentPlacementPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-be1352af-9328-4a6e-8688-2abf0f97f30e)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
