# CalculateSnapTransformation(LineMate,Mate,Double,Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic698.html

---

calculate a transformation matrix, that can be used to transform the associated placement into snap position that means, that the position and/or orientation of the associated placement will change, so that this mate fits to the target mate.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Matrix3D CalculateSnapTransformation( 
   LineMate pTargetMate,
   Mate additionalTargetMate,
   double dXOffset,
   double dYOffset,
   double dZOffset
)
```
```

```
```
public:
Matrix3D CalculateSnapTransformation( 
   LineMate^ pTargetMate,
   Mate^ additionalTargetMate,
   double dXOffset,
   double dYOffset,
   double dZOffset
)
```
```

#### Parameters

*pTargetMate*
:   LineMate to snap to.

*additionalTargetMate*
:   additional Targetmate to take the local x Position from.

*dXOffset*


*dYOffset*


*dZOffset*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.SnappingFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SnappingFailedException.html) | Thrown when operation failed. Check exception message for more info. |



See Also

#### Reference

[PointMate Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate.html)
  
[PointMate Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate~CalculateSnapTransformation.html)