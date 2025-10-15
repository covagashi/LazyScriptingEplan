# AdjustVisibleName(FunctionBase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~AdjustVisibleName(FunctionBase).html

---

Evaluates for a given functionbase the visible name and visible name format from the fullname of the functionbase and sets these evaluated values at the functionbase-object

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool AdjustVisibleName( 

   FunctionBase pFunctionBase

)
```
```

```
```
public:

bool AdjustVisibleName( 

   FunctionBase^ pFunctionBase

)
```
```

#### Parameters

*pFunctionBase*
:   Function for which the name is evaluated.

#### Return Value

Returns false, if the instance name could not be evaluated and set due to nesting.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
