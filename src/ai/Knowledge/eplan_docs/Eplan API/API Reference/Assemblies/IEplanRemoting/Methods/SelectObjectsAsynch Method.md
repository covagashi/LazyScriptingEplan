# SelectObjectsAsynch Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~SelectObjectsAsynch.html

---

Select Objects in Ged.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void SelectObjectsAsynch( 

   string strFullProjectName,

   StringCollection objectIds,

   bool bDeselectAll

)
```
```

```
```
void SelectObjectsAsynch( 

   String^ strFullProjectName,

   StringCollection^ objectIds,

   bool bDeselectAll

)
```
```

#### Parameters

*strFullProjectName*
:   Full project path name.

*objectIds*
:   Ids of objects to select.

*bDeselectAll*
:   Deselect all objects which already selected.

Remarks

This call is executed asynchronously.
