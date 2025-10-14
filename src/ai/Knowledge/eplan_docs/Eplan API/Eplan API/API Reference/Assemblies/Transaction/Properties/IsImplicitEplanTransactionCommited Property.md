# IsImplicitEplanTransactionCommited Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~IsImplicitEplanTransactionCommited.html

---

Transaction property which returns true if an implicit Eplan transaction was started and finished during lifetime of current transaction.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsImplicitEplanTransactionCommited {get;}
```
```

```
```
public:
property bool IsImplicitEplanTransactionCommited {
   bool get();
}
```
```

#### Property Value

true, when there was an internal commit false, when no internal commit was performed



See Also

#### Reference

[Transaction Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction.html)
  
[Transaction Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction_members.html)