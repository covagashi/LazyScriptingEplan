# NestedFunctions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~NestedFunctions.html

---

Returns an array of nested functions of the given main function. Nested-functions property returns functions whose identifying device tag contains the device tag of the parent + nested part of device tag.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Function[] NestedFunctions {get;}
```
```

```
```
public:
property array<Function^>^ NestedFunctions {
   array<Function^>^ get();
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the internal query throws an exception. |

Remarks

Returns array of functions of the next nesting level within main function. Only main functions can have nested functions. In case this function is not main, an empty array is returned.



See Also

#### Reference

[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[Function Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function_members.html)
  
[Function Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)
  
[IsMainFunction Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsMainFunction.html)