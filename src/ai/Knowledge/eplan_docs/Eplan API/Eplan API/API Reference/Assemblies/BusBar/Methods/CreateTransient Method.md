# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~CreateTransient.html

---

Creates not placed bended bus bar object with given bending radius and path.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static BusBar CreateTransient( 
   Project oProject,
   string strArticleNr,
   string strVariant,
   string strPathFileToUse,
   double dBendingRadius,
   Placement3D pCopperBundle,
   List<Placement3D> listOfAdditionalObjects
)
```
```

```
```
public:
static BusBar^ CreateTransient( 
   Project^ oProject,
   String^ strArticleNr,
   String^ strVariant,
   String^ strPathFileToUse,
   double dBendingRadius,
   Placement3D^ pCopperBundle,
   List<Placement3D^>^ listOfAdditionalObjects
)
```
```

#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*strPathFileToUse*
:   Full path with extension ("\*.fp1") to file containing a path. Can't be null or have zero length.

*dBendingRadius*
:   Bending radius. Must be grater then zero.

*pCopperBundle*
:   Copper bundle as parent of bended bus.

*listOfAdditionalObjects*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used. If copper bundle is null new copper bundle will be created.



See Also

#### Reference

[BusBar Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar.html)
  
[BusBar Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar_members.html)