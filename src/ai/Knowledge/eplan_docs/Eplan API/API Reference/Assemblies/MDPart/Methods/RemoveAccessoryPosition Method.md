# RemoveAccessoryPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveAccessoryPosition.html

---

Removes the given accessory position from the part.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void RemoveAccessoryPosition( 

   MDAccessoryPosition accessoryPos

)
```
```

```
```
public:

void RemoveAccessoryPosition( 

   MDAccessoryPosition^ accessoryPos

)
```
```

#### Parameters

*accessoryPos*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if `accessoryPos` is `null`. |

Remarks

accessoryPos: The accessory position that will be removed
