# CanImport Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~CanImport.html

---

Indicates whether the converter can convert external formats to XML.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
bool CanImport( 
   Context oContext,
   ref bool bSupportsProgress
)
```
```

```
```
bool CanImport( 
   Context^ oContext,
   bool% bSupportsProgress
)
```
```

#### Parameters

*oContext*
:   Context with parameters

*bSupportsProgress*
:   Indicates whether the converter supports a progress bar.

#### Return Value

true: conversion is possible; false: conversion is not possible



See Also

#### Reference

[IXMLProcessor Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor.html)
  
[IXMLProcessor Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor_members.html)