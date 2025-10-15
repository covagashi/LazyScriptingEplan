# CreateTransient(Project,String,String,Double,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic476.html

---

Creates transient and not placed Duct object with given length.

Syntax

**C#**
**C++/CLI**


public static Duct CreateTransient( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   double dLength,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Duct^ CreateTransient( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   double dLength,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*dLength*
:   Length of duct. Must be grater then zero.

*listOfAdditionalObjects*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the duct cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
