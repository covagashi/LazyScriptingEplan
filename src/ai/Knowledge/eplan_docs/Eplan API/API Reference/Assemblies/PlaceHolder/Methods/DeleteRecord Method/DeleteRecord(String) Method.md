# DeleteRecord(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~DeleteRecord(String).html

---

Deletes a record.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void DeleteRecord( 

   string strRecordName

)
```
```

```
```
public:

virtual void DeleteRecord( 

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
