# ConvertCoordinate(Page,CoordinateSystems,PointD,CoordinateSystems) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1327.html

---

Create a new device.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CreateDevice( 

   Project oProject,

   string strPartNumber,

   string strPartVariant,

   FunctionPropertyList pLocationList,

   ref List<IFunctionBase> oFunctionsList

)
```
```

```
```
public:

void CreateDevice( 

   Project^ oProject,

   String^ strPartNumber,

   String^ strPartVariant,

   FunctionPropertyList^ pLocationList,

   List<IFunctionBase^>^% oFunctionsList

)
```
```

#### Parameters

*oProject*
:   Project in which the new device will be.

*strPartNumber*
:   Part number.

*strPartVariant*
:   Part variant. If not existing variant is specified, then by default is selected a first available part's variant.

*pLocationList*
:   Property list fot the hierarchy properties. This parameter may be NULL. If the parameter is NULL or the list doesn't contain code letter and counter properties, the name of the device will be generated in accordance to the device numeration settings.

*oFunctionsList*
:   List of [Eplan.EplApi.DataModel.IFunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IFunctionBase.html) to which created functions will be stored.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid arguments. |
| **ArgumentNullException** | Is thrown, if some of the arguments are NULL. |
| **ApplicationException** | A necessary internal interface for creating devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while creating a device. |

Remarks

Method stores both 2D, and 3D objects to passed List of [Eplan.EplApi.DataModel.IFunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IFunctionBase.html).
