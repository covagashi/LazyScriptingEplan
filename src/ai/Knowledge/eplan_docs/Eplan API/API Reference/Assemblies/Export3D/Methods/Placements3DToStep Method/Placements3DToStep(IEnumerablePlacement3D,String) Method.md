# Placements3DToStep(IEnumerable<Placement3D>,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~Placements3DToStep(IEnumerable{Placement3D},String).html

---

Exports given article placements into files in STEP format.

Syntax

**C#**
**C++/CLI**


public bool Placements3DToStep( 

   IEnumerable<Placement3D> listPlacements3D,

   string strTargetDirectory

)

public:

bool Placements3DToStep( 

   IEnumerable<Placement3D^>^ listPlacements3D,

   String^ strTargetDirectory

)


#### Parameters

*listPlacements3D*
:   Collection of placements which will be exported. Can not be `null` or empty.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |

Remarks

Then names of files are generated from partnumber and variant. If there is no partnumber the name is created from part designation and identifying name. For all length-adjustable parts the legend ID is added. Export in original position of part without any transformation!
