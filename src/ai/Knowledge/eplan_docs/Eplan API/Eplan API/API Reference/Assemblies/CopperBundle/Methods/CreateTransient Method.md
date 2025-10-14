# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle~CreateTransient.html

---

Creates transient and not placed CopperBundle object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static CopperBundle CreateTransient( 
   Project oProject,
   List<Placement3D> listOfAdditionalObjects
)
```
```

```
```
public:
static CopperBundle^ CreateTransient( 
   Project^ oProject,
   List<Placement3D^>^ listOfAdditionalObjects
)
```
```

#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*listOfAdditionalObjects*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the CopperBundle cannot be created. |



See Also

#### Reference

[CopperBundle Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle.html)
  
[CopperBundle Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle_members.html)