# Equals Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html

---

Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override bool Equals( 
   object obj
)
```
```

```
```
public:
bool Equals( 
   Object^ obj
) override
```
```

#### Parameters

*obj*
:   StorableObject to compare

#### Return Value

true : Both objects are representing the same object in the project

false : Objects are representing different objects in the project or one of them is `null`.



See Also

#### Reference

[StorableObject Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)
  
[StorableObject Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject_members.html)