# GetSegmentPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentPlacements.html

---

Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public SegmentPlacement[] GetSegmentPlacements( 
   SegmentPlacementsFilter pFilter
)
```
```

```
```
public:
array<SegmentPlacement^>^ GetSegmentPlacements( 
   SegmentPlacementsFilter^ pFilter
)
```
```

#### Parameters

*pFilter*
:   Object used cusomize the results. If `null` then all segment placements for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the filter.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |



See Also

#### Reference

[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[DMObjectsFinder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder_members.html)
  
[SegmentPlacement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html)
  
[SegmentPlacementsFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentPlacementsFilter.html)