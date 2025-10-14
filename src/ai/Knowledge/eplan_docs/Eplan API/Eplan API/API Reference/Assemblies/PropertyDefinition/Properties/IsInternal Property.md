# IsInternal Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsInternal.html

---

Allows to check if a given property is marked as internal. Don't use this property.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsInternal {get;}
```
```

```
```
public:
property bool IsInternal {
   bool get();
}
```
```

#### Property Value

â¢ true = Property is internal

â¢ false = Property is not internal

Remarks

Can only be called after retrieving a property list from the given API class.

Example

- [C#](#i-tab-content-afcf2269-9e40-4573-a6bb-da695e2218cf)

```

Function function = page.Functions[0]; // A valid Function object

bool isInternal = function.Properties.FUNC_COUNTER.Definition.IsInternal;


```

See Also

#### Reference

[PropertyDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition.html)
  
[PropertyDefinition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition_members.html)