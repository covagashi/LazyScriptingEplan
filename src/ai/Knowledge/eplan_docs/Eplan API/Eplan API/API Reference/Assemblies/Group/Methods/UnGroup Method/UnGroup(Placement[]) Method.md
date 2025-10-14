# UnGroup(Placement[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup(Placement[]).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void UnGroup( 
   Placement[] placements
)
```
```

```
```
public:
void UnGroup( 
   array<Placement^>^ placements
)
```
```

#### Parameters

*placements*

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".



See Also

#### Reference

[Group Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)
  
[Group Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup.html)
  
[Placement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)