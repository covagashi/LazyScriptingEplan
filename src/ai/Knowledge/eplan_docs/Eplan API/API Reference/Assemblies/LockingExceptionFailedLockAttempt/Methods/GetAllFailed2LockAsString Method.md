# GetAllFailed2LockAsString Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt~GetAllFailed2LockAsString.html

---

returns all object ids of the objects which were not locked. In case this exception was produced while accessing unlocked object in write mode, only one object will be returned (the one which was accessed first).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override string[] GetAllFailed2LockAsString()
```
```

```
```
public:

array<String^>^ GetAllFailed2LockAsString(); override
```
```
