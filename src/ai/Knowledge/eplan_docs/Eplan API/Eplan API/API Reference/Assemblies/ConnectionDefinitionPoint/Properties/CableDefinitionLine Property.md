# CableDefinitionLine Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~CableDefinitionLine.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) from this [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Cable CableDefinitionLine {get;}
```
```

```
```
public:
property Cable^ CableDefinitionLine {
   Cable^ get();
}
```
```

#### Property Value

Cable definition related to this ConnectionDefinitionPoint.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the cable. |



See Also

#### Reference

[ConnectionDefinitionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)
  
[ConnectionDefinitionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint_members.html)
  
[Cable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html)