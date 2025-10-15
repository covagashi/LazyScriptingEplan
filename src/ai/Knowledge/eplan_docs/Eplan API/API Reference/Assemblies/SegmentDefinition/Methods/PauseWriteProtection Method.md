# PauseWriteProtection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~PauseWriteProtection.html

---

Temporarily disables write protection. Note that current write protection flags are not cleared.

Syntax

**C#**
**C++/CLI**


public virtual void PauseWriteProtection( 

   bool bPause

)

public:

virtual void PauseWriteProtection( 

   bool bPause

)


#### Parameters

*bPause*

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.WriteProtectionNotSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionNotSet.html) | Thrown if object has no write protectection. |
