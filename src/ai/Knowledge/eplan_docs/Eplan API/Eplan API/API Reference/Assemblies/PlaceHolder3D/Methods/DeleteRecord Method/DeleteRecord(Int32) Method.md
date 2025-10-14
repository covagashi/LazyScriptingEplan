# DeleteRecord(Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~DeleteRecord(Int32).html

---

Deletes a record.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void DeleteRecord( 
   int iPos
)
```
```

```
```
public:
virtual void DeleteRecord( 
   int iPos
)
```
```

#### Parameters

*iPos*
:   Index of the record.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments, e.g. if the record does not exist. |

Remarks

After deleting a record, the indices of the existing records are invalid and have to determined again using FindRecord.



See Also

#### Reference

[PlaceHolder3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)
  
[PlaceHolder3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~DeleteRecord.html)