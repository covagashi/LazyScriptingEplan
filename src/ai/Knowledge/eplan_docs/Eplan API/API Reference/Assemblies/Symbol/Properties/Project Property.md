# Project Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Symbol~Project.html

---

Returns the project to which the StorableObject belongs.

Syntax

**C#**
**C++/CLI**


public override Project Project {get;}

public:

property Project^ Project {

   Project^ get() override;

}


#### Property Value

The project to which the StorableObject belongs,

`null` if the StorableObject is transient or if the StorableObject does not belong to the objects of the project (PropertyPlacement with default scheme).
