Indicates whether the converter provides an export option.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
bool CanExport( 
   Context oContext,
   ref bool bSupportsProgress
)
```
```

```
```
bool CanExport( 
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

true: export is possible; false: export is not possible



See Also

#### Reference

[IXMLProcessor Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor.html)
  
[IXMLProcessor Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor_members.html)