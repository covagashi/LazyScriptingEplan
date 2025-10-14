# CreateTransient(Project,Double,Double,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic489.html

---

Creates transient and not placed, article free MountingPanel object with given dimensions.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static MountingPanel CreateTransient( 
   Project oProject,
   double dHeight,
   double dWidth,
   double dDepth,
   List<Placement3D> listOfAdditionalObjects
)
```
```

```
```
public:
static MountingPanel^ CreateTransient( 
   Project^ oProject,
   double dHeight,
   double dWidth,
   double dDepth,
   List<Placement3D^>^ listOfAdditionalObjects
)
```
```

#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*dHeight*


*dWidth*
:   Length of the MountingPanel. Must be grater then zero.

*dDepth*


*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created MountingPanel object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |



See Also

#### Reference

[MountingPanel Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel.html)
  
[MountingPanel Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~CreateTransient.html)