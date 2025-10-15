# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.AuxiliaryLine~Create.html

---

Creates not placed AuxiliaryLine object with defined start and end position.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static AuxiliaryLine Create( 

   Project pProject,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)
```
```

```
```
public:

static AuxiliaryLine^ Create( 

   Project^ pProject,

   PointD3D oStartPoint,

   PointD3D oEndPoint

)
```
```

#### Parameters

*pProject*
:   Project to which this object will be assign. Can't be null.

*oStartPoint*
:   Position of the object beginning.

*oEndPoint*
:   Position of the AuxiliaryLine end.

#### Return Value

Created and stored in database AuxiliaryLine object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |
