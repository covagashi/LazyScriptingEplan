# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoopFunction~Properties.html

---

EPLAN properties of the PCTLoopFunction object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PCTLoopFunctionPropertyList Properties {get;}
```
```

```
```
public:

new property PCTLoopFunctionPropertyList^ Properties {

   PCTLoopFunctionPropertyList^ get();

}
```
```

Example

- [C#](#i-tab-content-a04bc407-ea19-49da-9742-69267fc193bc)

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
