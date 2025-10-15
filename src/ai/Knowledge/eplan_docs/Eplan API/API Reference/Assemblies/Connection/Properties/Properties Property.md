# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Properties.html

---

.NET Property enabling access to P8 properties of the Connection object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new ConnectionPropertyList Properties {get;}
```
```

```
```
public:

new property ConnectionPropertyList^ Properties {

   ConnectionPropertyList^ get();

}
```
```

#### Property Value

P8 properties of the Connection.

Example

- [C#](#i-tab-content-27eaf072-1884-4c9e-9d88-72d6d5564b59)

```
Connection conn;//a valid connection

conn.Properties[Properties.Connection.DESIGNATION_PLANT] = "AP";

conn.Properties[Properties.Connection.CONNECTION_NAME] = "Connection name";

string name = conn.Properties[Properties.Connection.CONNECTION_NAME];
```
