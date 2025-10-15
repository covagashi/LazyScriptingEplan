# Correct(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~Correct(String,Boolean).html

---

Correct translations in project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Correct( 

   string strProjectName,

   bool bConvertAlreadyTranslatedTexts

)
```
```

```
```
public:

void Correct( 

   String^ strProjectName,

   bool bConvertAlreadyTranslatedTexts

)
```
```

#### Parameters

*strProjectName*
:   Full path to project from which texts will be corrected.

*bConvertAlreadyTranslatedTexts*
:   When set to `true` already converted texts are also translated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown when project is invalid or do not exist. |
| **ArgumentNullException** | Thrown when project is `null`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an error occurred during correction. |

Remarks

Method coresponds to Project->Translation->Extent in GUI and uses project settings to determine which texts should be corrected.
