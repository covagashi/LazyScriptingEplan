# IsNamePart Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsNamePart.html

---

Allows to check if a given property is name part.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsNamePart {get;}
```
```

```
```
public:

property bool IsNamePart {

   bool get();

}
```
```

#### Property Value

â¢ true = Property is name part

â¢ false = Property is not name part

Remarks

Can only be called after retrieving a property list from the given API class.

Example

- [C#](#i-tab-content-930b924d-051f-4421-af06-92914775995a)

```


Function function = page.Functions[0]; // A valid Function object



bool isNamePart = function.Properties.FUNC_COUNTER.Definition.IsNamePart;





```
