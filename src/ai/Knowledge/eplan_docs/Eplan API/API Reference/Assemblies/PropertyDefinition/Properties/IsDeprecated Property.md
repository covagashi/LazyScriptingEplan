# IsDeprecated Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsDeprecated.html

---

Allows to check if a given property is marked as deprecated.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool IsDeprecated {get;}
```
```

```
```
public:

virtual property bool IsDeprecated {

   bool get();

}
```
```

#### Property Value

â¢ true = Property is deprecated

â¢ false = Property is not deprecated

Remarks

Can only be called after retrieving a property list from the given API class. Returns false for user-defined properties.

Example

- [C#](#i-tab-content-44cd7e4d-fcaa-4167-a57d-57082e9882b0)

```


Function function = page.Functions[0]; // A valid Function object



bool isDeprecated = function.Properties.FUNC_COUNTER.Definition.IsDeprecated;





```
