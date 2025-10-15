# RemovePLCAddress Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemovePLCAddress.html

---

Removes existing PLC input or output from this planning object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void RemovePLCAddress( 

   PlanningSegment.PLCAddress pPLCAddress

)
```
```

```
```
public:

void RemovePLCAddress( 

   PlanningSegment.PLCAddress^ pPLCAddress

)
```
```

#### Parameters

*pPLCAddress*
:   PLCAddress which will be removed. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter is `null`. |
| [System.InvalidOperationException](#) | Thrown if PLCAddress is appended from another parent. |

Example

- [C#](#i-tab-content-1efda84a-511d-496d-bd18-c255050be800)

```
//get object which will be removed

PlanningSegment.PLCAddress oAddress = oPCTLoop.PLCAddresses[0];



//remove object from planning object

oPCTLoop.RemovePLCAddress(oAddress);



```
