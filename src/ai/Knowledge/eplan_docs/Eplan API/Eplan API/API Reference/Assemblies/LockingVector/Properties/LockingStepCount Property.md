# LockingStepCount Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector~LockingStepCount.html

---

Returns the number of active LockingSteps. This is not the length of the vector, because the locking-operations are stored(represented) there (not the LockingSteps).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int LockingStepCount {get;}
```
```

```
```
public:
property int LockingStepCount {
   int get();
}
```
```

#### Property Value

Returns the number of started LockingStep objects (and not ended).



See Also

#### Reference

[LockingVector Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector.html)
  
[LockingVector Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingVector_members.html)
  
[LockingStep Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingStep.html)