# UnGroup(Placement[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup(Placement[],Boolean).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group.

Syntax

**C#**
**C++/CLI**


public void UnGroup( 

   Placement[] placements,

   bool bRemoveEmptyGroup

)

public:

void UnGroup( 

   array<Placement^>^ placements,

   bool bRemoveEmptyGroup

)


#### Parameters

*placements*


*bRemoveEmptyGroup*
:   If true method will remove also Group when it becomes empty.

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".
