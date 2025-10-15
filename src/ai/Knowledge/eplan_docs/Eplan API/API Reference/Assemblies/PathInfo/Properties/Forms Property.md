# Forms Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo~Forms.html

---

Returns default Forms directory.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string Forms {get;}
```
```

```
```
public:

property String^ Forms {

   String^ get();

}
```
```

#### Property Value

string : default Forms directory

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown when the directory cannot be obtained from settings. |
