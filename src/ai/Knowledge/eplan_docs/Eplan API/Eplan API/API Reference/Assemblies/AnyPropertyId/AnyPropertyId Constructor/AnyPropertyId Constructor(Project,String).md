# AnyPropertyId Constructor(Project,String)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId~_ctor(Project,String).html

---

Constructor. Creates the AnyPropertyId object from user-defined property identifying name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public AnyPropertyId( 
   Project pProject,
   string strUserDefiniedPropertyIdentName
)
```
```

```
```
public:
AnyPropertyId( 
   Project^ pProject,
   String^ strUserDefiniedPropertyIdentName
)
```
```

#### Parameters

*pProject*
:   Project in which user-defined property is created.

*strUserDefiniedPropertyIdentName*
:   Identifying name of user-defined property.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when pProject or strUserDefiniedPropertyIdentName is null. |
| [System.ArgumentException](#) | Thrown when pProject is invalid. |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | Thrown when property was not found. |



See Also

#### Reference

[AnyPropertyId Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html)
  
[AnyPropertyId Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId~_ctor.html)