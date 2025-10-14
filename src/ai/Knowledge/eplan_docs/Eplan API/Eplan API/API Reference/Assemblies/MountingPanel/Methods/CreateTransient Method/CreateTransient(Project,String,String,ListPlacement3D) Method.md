# CreateTransient(Project,String,String,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic488.html

---

Creates transient and not placed MountingPanel object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static MountingPanel CreateTransient( 
   Project oProject,
   string strArticleNr,
   string strVariant,
   List<Placement3D> listOfAdditionalObjects
)
```
```

```
```
public:
static MountingPanel^ CreateTransient( 
   Project^ oProject,
   String^ strArticleNr,
   String^ strVariant,
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

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created MountingPanel object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exceptions message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the MountingPanel cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.



See Also

#### Reference

[MountingPanel Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel.html)
  
[MountingPanel Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPanel~CreateTransient.html)