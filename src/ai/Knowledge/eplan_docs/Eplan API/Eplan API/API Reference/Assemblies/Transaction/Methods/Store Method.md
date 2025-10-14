# Store Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~Store.html

---

This method will enable to commit the transaction, and \internal open the next transaction.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Store()
```
```

```
```
public:
void Store();
```
```

Example

Store() usage example. In this example Function f Name is set "F1", Description is set "generic function". The changes are stored in the project. Name "F2" is not committed, so it is not stored.

- [C#](#i-tab-content-fcc3837e-7964-458f-a10d-2239e1fabda2)

```
using (Transaction txn = new TransactionManager().CreateTransaction())
{
    Function f;
    f.Name = "F1";
    f.Description = "generic function";
    txn.Store();
    f.Name = "F2";
    txn.Abort();
}
```

See Also

#### Reference

[Transaction Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction.html)
  
[Transaction Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction_members.html)