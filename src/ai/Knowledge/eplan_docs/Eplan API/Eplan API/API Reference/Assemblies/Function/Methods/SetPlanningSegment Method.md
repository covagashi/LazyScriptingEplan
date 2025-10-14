# SetPlanningSegment Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SetPlanningSegment.html

---

Assigns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) to this function.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetPlanningSegment( 
   PlanningSegment pPlanningSegment,
   bool bWriteArticleRefToFunction
)
```
```

```
```
public:
void SetPlanningSegment( 
   PlanningSegment^ pPlanningSegment,
   bool bWriteArticleRefToFunction
)
```
```

#### Parameters

*pPlanningSegment*
:   [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) which will be assigned to function, or `null` to remove planning object from function.

*bWriteArticleRefToFunction*
:   If `true` and this is main function then article reference from planning object is written to function as main article.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [System.InvalidOperationException](#) | Thrown when object of type [Eplan.EplApi.DataModel.Planning.StructureSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.StructureSegment.html) is being assigned to function. |



See Also

#### Reference

[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[Function Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function_members.html)