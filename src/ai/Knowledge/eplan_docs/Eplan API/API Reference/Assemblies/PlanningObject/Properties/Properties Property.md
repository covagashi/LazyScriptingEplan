# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject~Properties.html

---

EPLAN properties of the PlanningObject object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PlanningObjectPropertyList Properties {get;}
```
```

```
```
public:

new property PlanningObjectPropertyList^ Properties {

   PlanningObjectPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-5c59f2a0-f550-413b-b317-8dcc0e564a1c)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
