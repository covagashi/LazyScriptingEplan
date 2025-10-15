# CreateDrillingViews Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateDrillingViews.html

---

Creates drilling views report

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CreateDrillingViews( 

   Project oProject,

   StringCollection colTemplates,

   bool bReplaceExisting

)
```
```

```
```
public:

void CreateDrillingViews( 

   Project^ oProject,

   StringCollection^ colTemplates,

   bool bReplaceExisting

)
```
```

#### Parameters

*oProject*
:   Project

*colTemplates*
:   Collection of templates

*bReplaceExisting*
:   Replace existing drilling views when true

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any of parameters is null. |
| [System.ArgumentException](#) | If any of parameters is invalid. |
| [System.ApplicationException](#) | Failed to create. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating. Please refer to the error message. |

Example

- [C#](#i-tab-content-a451d806-b3b6-4538-a67e-3da8d83594e7)

```
StringCollection oTemplates = new StringCollection();

oTemplates.Add("1");

new Reports().CreateDrillingViews(m_oProject, oTemplates, true);
```
