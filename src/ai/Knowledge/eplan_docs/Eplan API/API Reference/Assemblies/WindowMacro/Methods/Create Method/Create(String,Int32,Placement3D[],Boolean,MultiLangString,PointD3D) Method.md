# Create(String,Int32,Placement3D[],Boolean,MultiLangString,PointD3D) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic741.html

---

Writes a window macro file from the pPlacements if at least one given object is valid. Created macro is opened.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 

   string macroFileName,

   int nVariant,

   Placement3D[] pPlacements,

   bool bAddChildren,

   MultiLangString strDescription

)
```
```

```
```
public:

void Create( 

   String^ macroFileName,

   int nVariant,

   array<Placement3D^>^ pPlacements,

   bool bAddChildren,

   MultiLangString^ strDescription

)
```
```

#### Parameters

*macroFileName*
:   The name (including path) for the macro file. Parameter value must include a valid extension (otherwise an exception is thrown).

*nVariant*
:   The variant written (A file can contain more than one variants)

*pPlacements*
:   The placements the macro should contain. They should be from the same page.

*bAddChildren*


*strDescription*
:   The description for this macro file or null when no description should be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid |

Remarks

Reference point used in macro is calculated automatically by P8.
