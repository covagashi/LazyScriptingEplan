# CableConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable~CableConnections.html

---

Returns an array of Connection objects that exist under the cable definition line represented by this Cable object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Connection[] CableConnections {get;}
```
```

```
```
public:
property array<Connection^>^ CableConnections {
   array<Connection^>^ get();
}
```
```

Remarks

To associate a Cable with its Connections, Name and VisibleName should be set the same in Cable as in ConnectionDefinitionPoints.



See Also

#### Reference

[Cable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable.html)
  
[Cable Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Cable_members.html)
  
[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)