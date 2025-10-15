# GetFirstEmbeddedInstance Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine~GetFirstEmbeddedInstance.html

---

Returns first instance embedded in this line.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Placement GetFirstEmbeddedInstance()
```
```

```
```
public:

Placement^ GetFirstEmbeddedInstance();
```
```

#### Return Value

`null` when there is no instance embedded

first embedded instance

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when first embedded instance cannot be read. |
