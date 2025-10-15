# AdditionalConnections Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint~AdditionalConnections.html

---

.NET Property enabling access to additional connections of the net not stored at this NetDefinitionPoint

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Connection[] AdditionalConnections {get;}
```
```

```
```
public:

property array<Connection^>^ AdditionalConnections {

   array<Connection^>^ get();

}
```
```

#### Property Value

All connections of the net not defined in NetDefinitionPoint
