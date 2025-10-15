# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.RoutingSegment~CreateTransient.html

---

Create new routing segment in P8 project.

Syntax

**C#**
**C++/CLI**


public void CreateTransient( 

   InstallationSpace pInstallationSpace

)

public:

void CreateTransient( 

   InstallationSpace^ pInstallationSpace

)


#### Parameters

*pInstallationSpace*

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the RoutingSegment has already been created. |
| [System.ArgumentNullException](#) | Thrown if parameter `pInstallationSpace` is `null`. |

Remarks

Method creates new routing segment and sets given installation space as its parent.
