# SubConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~SubConnections.html

---

If connection contains interruption points, this method returns an array of partial connections which current connection consists of For a "net connection" this method will return an empty array.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Connection[] SubConnections {get;}
```
```

```
```
public:
property array<Connection^>^ SubConnections {
   array<Connection^>^ get();
}
```
```



See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)