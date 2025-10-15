# ImportDeviceList(String,String,Format) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDeviceList(String,String,Format).html

---

This function imports a device list into a given project.

Syntax

**C#**
**C++/CLI**


public void ImportDeviceList( 

   string strFullLinkFileName,

   string strImportFilePath,

   DeviceService.Format fileFormat

)

public:

void ImportDeviceList( 

   String^ strFullLinkFileName,

   String^ strImportFilePath,

   DeviceService.Format fileFormat

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project into which the device list will be imported.

*strImportFilePath*
:   Full file name of the device list file to import.

*fileFormat*
:   Format of the import file\: By default the following file formats are available\: XML or CSV. The enum FILE\_FORMAT defines the available values. If an invalid format is set, the file is expected to be XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing a device list could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of a device list. Please refer to the exception message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidConverter](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidConverter.html) | Thrown when given parameter  `fileFormat`  isn't valid converter or such conversion doesn't exist at all. |
