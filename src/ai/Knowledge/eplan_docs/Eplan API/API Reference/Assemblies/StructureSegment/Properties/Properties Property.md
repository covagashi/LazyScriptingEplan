# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.StructureSegment~Properties.html

---

EPLAN properties of the StructureSegment object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new StructureSegmentPropertyList Properties {get;}
```
```

```
```
public:

new property StructureSegmentPropertyList^ Properties {

   StructureSegmentPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-0d82535e-111c-4cd1-a90d-416ea560ed1d)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
