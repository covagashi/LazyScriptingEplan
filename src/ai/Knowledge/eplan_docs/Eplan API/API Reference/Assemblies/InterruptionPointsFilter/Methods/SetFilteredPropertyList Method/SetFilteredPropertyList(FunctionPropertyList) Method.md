# SetFilteredPropertyList(FunctionPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~SetFilteredPropertyList(FunctionPropertyList).html

---

Sets the [InterruptionPointPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList.html) that [InterruptionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)s matching the filter must have.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetFilteredPropertyList( 

   FunctionPropertyList searchedPropList

)
```
```

```
```
public:

void SetFilteredPropertyList( 

   FunctionPropertyList^ searchedPropList

)
```
```

#### Parameters

*searchedPropList*
:   List of the P8 properties the [InterruptionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
