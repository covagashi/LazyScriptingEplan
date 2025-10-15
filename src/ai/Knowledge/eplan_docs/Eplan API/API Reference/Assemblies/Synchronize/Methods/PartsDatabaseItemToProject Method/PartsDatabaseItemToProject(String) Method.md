# PartsDatabaseItemToProject(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartsDatabaseItemToProject(String).html

---

Synchronizes the database items (like parts, manufactures addresses, etc.) stored in the project with the items in the parts master database. This function updates items inside project; items in the database are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize".

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void PartsDatabaseItemToProject( 

   string strFullLinkFileName

)
```
```

```
```
public:

void PartsDatabaseItemToProject( 

   String^ strFullLinkFileName

)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project for which the database items will be updated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the synchronization process and will be closed subsequently.
