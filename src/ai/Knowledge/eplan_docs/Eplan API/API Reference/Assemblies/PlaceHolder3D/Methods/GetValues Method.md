# GetValues Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~GetValues.html

---

\Returns the values of all variables in the nIndex-th PlaceHolder3D of a Macro variant for a given record.

Syntax

**C#**
**C++/CLI**


public virtual StringCollection GetValues( 

   string strRecordName

)

public:

virtual StringCollection^ GetValues( 

   String^ strRecordName

)


#### Parameters

*strRecordName*
:   Record name.

#### Return Value

The values of the variables.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |
