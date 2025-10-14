# RemoveSubPlacement(Placement) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacement(Placement).html

---

Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) from the group and from the project. The Placement object passed into this method is no longer valid.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void RemoveSubPlacement( 
   Placement placement
)
```
```

```
```
public:
virtual void RemoveSubPlacement( 
   Placement^ placement
)
```
```

#### Parameters

*placement*

Remarks

This method doesn't make sense for class "SymbolVariant" and "DimensionGroup". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant" and "DimensionGroup".



See Also

#### Reference

[Group Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)
  
[Group Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacement.html)
  
[Placement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)