# SetNeededSteps Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~SetNeededSteps.html

---

Indicates how many steps are required to reach 100%. E.g. used for loops.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetNeededSteps( 
   int neededSteps
)
```
```

```
```
public:
void SetNeededSteps( 
   int neededSteps
)
```
```

#### Parameters

*neededSteps*
:   Number of steps

Remarks

Caution: Keep in mind to call this function after having created a new segment ([BeginPart](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~BeginPart.html)). Otherwise no steps are implemented.



See Also

#### Reference

[Progress Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress.html)
  
[Progress Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress_members.html)