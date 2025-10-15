# GetAllFailed2LockAsString Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException~GetAllFailed2LockAsString.html

---

returns all object ids of the objects which were not locked. In case this exception was produced while accessing unlocked object in write mode, only one object will be returned (the one which was accessed first).

Syntax

**C#**
**C++/CLI**


public virtual string[] GetAllFailed2LockAsString()

public:

virtual array<String^>^ GetAllFailed2LockAsString();

