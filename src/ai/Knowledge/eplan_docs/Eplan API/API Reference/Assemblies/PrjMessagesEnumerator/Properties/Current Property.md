# Current Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesEnumerator~Current.html

---

gets the current element in [Eplan::EplApi::EServices:](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection.html)

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual object Current {get;}
```
```

```
```
public:

virtual property Object^ Current {

   Object^ get();

}
```
```

#### Property Value

the current element

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when the enumerator is positioned before the first element of the collection or after the last element. |

Remarks

must be called to advance the enumerator to the first element of the collection before reading the current value
