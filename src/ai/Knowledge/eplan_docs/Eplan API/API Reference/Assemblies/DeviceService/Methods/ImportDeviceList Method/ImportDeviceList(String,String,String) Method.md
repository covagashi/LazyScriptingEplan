# ImportDeviceList(String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDeviceList(String,String,String).html

---

This function imports a device list into a given project.

Syntax

**C#**
**C++/CLI**


public void ImportDeviceList( 

   string strFullLinkFileName,

   string strImportFilePath,

   string strConverter

)

public:

void ImportDeviceList( 

   String^ strFullLinkFileName,

   String^ strImportFilePath,

   String^ strConverter

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project into which the device list will be imported.

*strImportFilePath*
:   Full file name of the device list file to import.

*strConverter*
:   Converter long name, see [XPamImportXml](XPamImportXml.html) converters

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing a device list could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of a device list. Please refer to the exception message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidConverter](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidConverter.html) | Thrown when given parameter  `strConverter`  isn't valid converter or such conversion dosesn't exist at all. |
