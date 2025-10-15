# RemoveConnectionPointPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemoveConnectionPointPosition.html

---

Removes connection point data stored under given index.

Syntax

**C#**
**C++/CLI**


public void RemoveConnectionPointPosition( 

   short iIndex

)

public:

void RemoveConnectionPointPosition( 

   short iIndex

)


#### Parameters

*iIndex*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `iIndex` value is less then `0`. |

Remarks

Index starts from 0.
