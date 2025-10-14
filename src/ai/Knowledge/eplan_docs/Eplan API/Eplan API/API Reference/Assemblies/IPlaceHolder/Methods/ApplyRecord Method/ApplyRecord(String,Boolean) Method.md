# ApplyRecord(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~ApplyRecord(String,Boolean).html

---

Applies a record of values on a PlaceHolder object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void ApplyRecord( 
   string strRecordName,
   bool bApplyPageAndProjectData
)
```
```

```
```
void ApplyRecord( 
   String^ strRecordName,
   bool bApplyPageAndProjectData
)
```
```

#### Parameters

*strRecordName*
:   Name of the record to apply.

*bApplyPageAndProjectData*
:   Whether the page and project data should be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |



See Also

#### Reference

[IPlaceHolder Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder.html)
  
[IPlaceHolder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~ApplyRecord.html)