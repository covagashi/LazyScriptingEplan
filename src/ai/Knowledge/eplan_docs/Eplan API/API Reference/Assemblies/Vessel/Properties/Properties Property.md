# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.Vessel~Properties.html

---

EPLAN properties of the Vessel object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new VesselPropertyList Properties {get;}
```
```

```
```
public:

new property VesselPropertyList^ Properties {

   VesselPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-b466e7f3-d59d-428d-ac33-3e482c27797f)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
