# CreateLink(PlanningSegment,PlanningSegment) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CreateLink(PlanningSegment,PlanningSegment).html

---

Creates a link between two given PlanningSegments.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static bool CreateLink( 

   PlanningSegment superiorSegment,

   PlanningSegment targetSegment

)
```
```

```
```
public:

static bool CreateLink( 

   PlanningSegment^ superiorSegment,

   PlanningSegment^ targetSegment

)
```
```

#### Parameters

*superiorSegment*
:   Segment under which a link will be created.

*targetSegment*
:   Segment which will be linked under superiorSegment.

#### Return Value

Returns false when PlanningSegments are from different projects.
