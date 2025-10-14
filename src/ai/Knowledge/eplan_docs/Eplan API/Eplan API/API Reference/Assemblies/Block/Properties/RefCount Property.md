# RefCount Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~RefCount.html

---

Number of references.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int RefCount {get;}
```
```

```
```
public:
property int RefCount {
   int get();
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when operation get has failed. |

Remarks

This field shows how many references to this block are placed in the project. (At present, only one reference can be created.)



See Also

#### Reference

[Block Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block.html)
  
[Block Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block_members.html)