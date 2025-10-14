# CableDefinitionLine Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CableDefinitionLine.html

---

Returns [Eplan.EplApi.DataModel.EObjects.Cable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html) from a [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection. If there are more then one [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) assigned to this Connection, an exception is thrown. Such situation has to be handled by calling [ConnectionDefPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~ConnectionDefPoints.html) and analyze of the result.

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

Cable definition related to this Connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Different count than 1 [ConnectionDefinitionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html) related to this Connection. |



See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)
  
[Cable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html)