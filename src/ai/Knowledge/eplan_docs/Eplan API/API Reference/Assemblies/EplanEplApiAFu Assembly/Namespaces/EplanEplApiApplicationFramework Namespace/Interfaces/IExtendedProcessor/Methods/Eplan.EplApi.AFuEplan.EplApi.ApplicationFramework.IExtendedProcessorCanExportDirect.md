Indicates whether the converter provides an export.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
bool CanExportDirect( 
   Context oContext,
   ref bool bSupportsProgress
)
```
```

```
```
bool CanExportDirect( 
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

