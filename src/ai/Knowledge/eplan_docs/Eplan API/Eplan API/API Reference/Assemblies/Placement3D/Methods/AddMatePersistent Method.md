# AddMatePersistent Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddMatePersistent.html

---

Add copy of a mate to a Placement3D.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void AddMatePersistent( 
   Mate pCustomMate
)
```
```

```
```
public:
void AddMatePersistent( 
   Mate^ pCustomMate
)
```
```

#### Parameters

*pCustomMate*
:   Mate which copy will be added to this placement. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |

Remarks

The method is used to add user-defined mate to a Placement3D. During adding a source mate, there is done some validation to keep following rules: \* If mate's logical type is UserGripPoint or UserGripPointExt, its name has to be 'G1'. \* UserGripPoint is the standard handle and gets always standard matching names. \* To prevent snapping on poles or holder of a bus bar system, most of source mates get the suffix '-#P#H' for matching mate names \* If there are no user-defined persistent mates, EPLAN creates some transient mates. For target mates, there are no limitation with defining the mate name and the matching names.



See Also

#### Reference

[Placement3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)
  
[Placement3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D_members.html)