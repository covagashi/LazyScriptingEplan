# DeleteRecord(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteRecord(String).html

---

Deletes a record.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void DeleteRecord( 
   string strRecordName
)
```
```

```
```
void DeleteRecord( 
   String^ strRecordName
)
```
```

#### Parameters

*strRecordName*
:   Name of the record to be deleted.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments, e.g. if the record does not exist. |

Remarks

After deleting a record, the indices of the existing records are invalid and have to determined again using FindRecord.



See Also

#### Reference

[IPlaceHolder Interface](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder.html)
  
[IPlaceHolder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~DeleteRecord.html)