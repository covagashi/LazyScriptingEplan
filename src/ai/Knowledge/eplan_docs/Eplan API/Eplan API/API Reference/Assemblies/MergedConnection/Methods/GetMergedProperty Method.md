# GetMergedProperty Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~GetMergedProperty.html

---

Returns value of merged property having given property id.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue GetMergedProperty( 
   AnyPropertyId propId
)
```
```

```
```
public:
PropertyValue^ GetMergedProperty( 
   AnyPropertyId^ propId
)
```
```

#### Parameters

*propId*
:   [AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) - id of property to read

#### Return Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) value of the property.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |



See Also

#### Reference

[MergedConnection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection.html)
  
[MergedConnection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection_members.html)
  
[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[AnyPropertyId Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html)