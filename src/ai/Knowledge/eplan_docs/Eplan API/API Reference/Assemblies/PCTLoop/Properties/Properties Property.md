# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoop~Properties.html

---

EPLAN properties of the PCTLoop object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PCTLoopPropertyList Properties {get;}
```
```

```
```
public:

new property PCTLoopPropertyList^ Properties {

   PCTLoopPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-dd40eb83-416d-47c9-815c-e8da9bf3b7f5)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
