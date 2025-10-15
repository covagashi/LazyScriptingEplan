# DoReassignWires(Function,Connection[],Boolean,AnyPropertyId[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1307.html

---

Method for numbering cables in a project.

Syntax

**C#**
**C++/CLI**


public void RenumberCables( 

   Function[] oCables,

   string strNumberingSchemeName,

   bool bKeepOldNames,

   bool bKeepIdentifier,

   int nStartValue,

   int nStepValue

)

public:

void RenumberCables( 

   array<Function^>^ oCables,

   String^ strNumberingSchemeName,

   bool bKeepOldNames,

   bool bKeepIdentifier,

   int nStartValue,

   int nStepValue

)


#### Parameters

*oCables*
:   An array of functions (cables, shildings) to number.

*strNumberingSchemeName*
:   Name of the scheme used for cable numbering.

*bKeepOldNames*
:   Keep existing cable DTs. If set to true, already existing cable DTs will not be changed, only cables with "?" character in the identifier will be numbered.

*bKeepIdentifier*
:   If set to true, the existing identifier will not be changed.

*nStartValue*
:   Start value for the device tag counter.

*nStepValue*
:   The device tag counter will be incremented by this value.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | The internal interface necessary for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. Please read the exception message.. |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |

Remarks

If the user scheme given in strNumberingSchemeName does not exist, an ArgumentException will be thrown. If you pass an empty string to strCreateSchemeName, the last-used scheme will be used which is currently set in GUI.
