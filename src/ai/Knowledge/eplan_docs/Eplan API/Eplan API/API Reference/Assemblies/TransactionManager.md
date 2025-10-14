# TransactionManager

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager.html

---

TransactionManager is a singleton class.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.TransactionManager**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class TransactionManager
```
```

```
```
public ref class TransactionManager
```
```

Remarks

For details, please refer to [Transactions](Transactions.html) chapter of API Help.

Example

Transaction manager usage example.

- [C#](#i-tab-content-393e4942-fc6b-4347-abe0-0ac96c4ff189)

```
using (Transaction txn = new TransactionManager().CreateTransaction())
{
Function f;
f.Name = "F1";			
txn.Commit();
}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [TransactionManager Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsEplanTransactionRunning](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~IsEplanTransactionRunning.html) | Tells if a P8 transaction is open. |
| Public Property | [IsTransactionRunning](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~IsTransactionRunning.html) | Tells if a read-write API transaction is open. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CreateTransaction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~CreateTransaction.html) | Creates object representing a read-write transaction. |

[Top](#top)




See Also

#### Reference

[TransactionManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[Transaction Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction.html)