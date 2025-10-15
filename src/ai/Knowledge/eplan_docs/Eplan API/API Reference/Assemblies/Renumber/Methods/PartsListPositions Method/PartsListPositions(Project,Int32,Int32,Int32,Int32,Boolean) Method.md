# PartsListPositions(Project,Int32,Int32,Int32,Int32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber~PartsListPositions(Project,Int32,Int32,Int32,Int32,Boolean).html

---

Method for renumbering Bill Of Materials positions.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void PartsListPositions( 

   Project pProject,

   int ePartsKind,

   int nStartValue,

   int nIncrement,

   int nFieldWidth,

   bool bSameNumbers

)
```
```

```
```
public:

void PartsListPositions( 

   Project^ pProject,

   int ePartsKind,

   int nStartValue,

   int nIncrement,

   int nFieldWidth,

   bool bSameNumbers

)
```
```

#### Parameters

*pProject*
:   Project in which the Bill Of Materials positions will be renumbered.

*ePartsKind*
:   Specifies which positions will be renumbered. Allowed values are \members from enumeration Parts, e.g. CableParts | ClampParts

*nStartValue*
:   Start value

*nIncrement*
:   Step width

*nFieldWidth*
:   Number of digits for a position.

*bSameNumbers*
:   Use same numbers for identical parts.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
