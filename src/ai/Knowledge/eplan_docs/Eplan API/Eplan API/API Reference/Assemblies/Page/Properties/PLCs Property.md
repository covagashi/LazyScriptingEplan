# PLCs Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PLCs.html

---

Returns all [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s placed on the page. If the filter was set up, returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching the filter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PLC[] PLCs {get;}
```
```

```
```
public:
property array<PLC^>^ PLCs {
   array<PLC^>^ get();
}
```
```

#### Property Value

[Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |



See Also

#### Reference

[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)
  
[Page Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page_members.html)
  
[PLC Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)
  
[Filter Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Filter.html)