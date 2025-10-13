returns all object ids of the objects which were not locked. In case this exception was produced while accessing unlocked object in write mode, only one object will be returned (the one which was accessed first).

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual string[] GetAllFailed2LockAsString()
```
```

```
```
public:
virtual array<String^>^ GetAllFailed2LockAsString();
```
```



See Also

#### Reference

[LockingException Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html)
  
[LockingException Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException_members.html)