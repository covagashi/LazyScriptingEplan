# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~Name.html

---

Returns the name of the FunctionBase.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual string Name {get; set;}
```
```

```
```
public:
virtual property String^ Name {
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
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the name cannot be retrieved from the function |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | FunctionBase is transient. |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |



See Also

#### Reference

[FunctionBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)
  
[FunctionBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase_members.html)