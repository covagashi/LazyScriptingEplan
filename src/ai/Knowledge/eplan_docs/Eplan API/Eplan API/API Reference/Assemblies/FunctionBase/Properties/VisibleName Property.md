# VisibleName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~VisibleName.html

---

Returns the visible name of the FunctionBase.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual string VisibleName {get; set;}
```
```

```
```
public:
virtual property String^ VisibleName {
   String^ get();
   void set (    String^ value);
}
```
```

#### Property Value

name of the function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the visible name cannot be retrieved from the function |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | FunctionBase is transient. |
| [System.ArgumentNullException](#) | Thrown while setting when the new value is `null`. |



See Also

#### Reference

[FunctionBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)
  
[FunctionBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase_members.html)
  
[IsTransient Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html)