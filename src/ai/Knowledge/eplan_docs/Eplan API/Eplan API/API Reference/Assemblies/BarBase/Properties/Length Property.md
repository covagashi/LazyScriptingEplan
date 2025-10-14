# Length Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BarBase~Length.html

---

Returns and sets length of this object. Length is stored in mm.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual double Length {get; set;}
```
```

```
```
public:
virtual property double Length {
   double get();
   void set (    double value);
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Length must be grater then zero. |
| [Eplan.EplApi.DataModel.OperationFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OperationFailedException.html) | Failed to set the length. |



See Also

#### Reference

[BarBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BarBase.html)
  
[BarBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BarBase_members.html)