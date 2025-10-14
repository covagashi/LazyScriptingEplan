# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceGroup~Create.html

---

Creates a new Group object. It is placed on the page of first placement given as parameter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override void Create( 
   Placement[] placements
)
```
```

```
```
public:
void Create( 
   array<Placement^>^ placements
) override
```
```

#### Parameters

*placements*
:   Placements that create the group.

Exceptions

| Exception | Description |
| --- | --- |
| [ElementFromWrongPageException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ElementFromWrongPageException.html) | Thrown when first placement doesn't have valid page. |
| [InsufficientElementsCountException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientElementsCountException.html) | Thrown when number of placements is less than two. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown in two cases: 1.When one of given placements is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). 2. When one of given placements is a parent group of it. |



See Also

#### Reference

[DeviceGroup Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceGroup.html)
  
[DeviceGroup Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceGroup_members.html)