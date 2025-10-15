# Parent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Parent.html

---

Gets or Sets parent object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PlanningSegment Parent {get; set;}
```
```

```
```
public:

property PlanningSegment^ Parent {

   PlanningSegment^ get();

   void set (    PlanningSegment^ value);

}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parent with its segemnt definition cannot be set for this object. |
