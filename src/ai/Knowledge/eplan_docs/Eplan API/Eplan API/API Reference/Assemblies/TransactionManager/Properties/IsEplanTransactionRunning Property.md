# IsEplanTransactionRunning Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~IsEplanTransactionRunning.html

---

Tells if a P8 transaction is open.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsEplanTransactionRunning {get;}
```
```

```
```
public:
property bool IsEplanTransactionRunning {
   bool get();
}
```
```

#### Property Value

true, when there is an opened Transaction false, when a transaction is not open

Remarks

P8 (or framework) transaction is a transaction which was started inside of framework.



See Also

#### Reference

[TransactionManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager.html)
  
[TransactionManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager_members.html)