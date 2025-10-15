# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Properties.html

---

EPLAN properties of the PlanningSegment object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PlanningSegmentPropertyList Properties {get;}
```
```

```
```
public:

new property PlanningSegmentPropertyList^ Properties {

   PlanningSegmentPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-d8fb854a-3f34-42b6-a2c5-31b5f69586c2)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
