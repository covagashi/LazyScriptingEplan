# SetFilteredPropertyList(SegmentPlacementPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic461.html

---

Sets the [Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList.html) that [Eplan.EplApi.DataModel.Planning.SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html)s matching the filter must have.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetFilteredPropertyList( 
   SegmentPlacementPropertyList searchedPropList
)
```
```

```
```
public:
void SetFilteredPropertyList( 
   SegmentPlacementPropertyList^ searchedPropList
)
```
```

#### Parameters

*searchedPropList*
:   List of the P8 properties the [Eplan.EplApi.DataModel.Planning.SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |



See Also

#### Reference

[SegmentPlacementsFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentPlacementsFilter.html)
  
[SegmentPlacementsFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentPlacementsFilter_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentPlacementsFilter~SetFilteredPropertyList.html)