# ExportDeviceList(String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ExportDeviceList(String,String,String).html

---

This function exports the device list of a given project. It is used for exporting devices from the planning list (but neither all devices from the project nor all from the bill of materials).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ExportDeviceList( 

   string strFullLinkFileName,

   string strExportFilePath,

   string strConverter

)
```
```

```
```
public:

void ExportDeviceList( 

   String^ strFullLinkFileName,

   String^ strExportFilePath,

   String^ strConverter

)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project from which the device list will be exported.

*strExportFilePath*
:   Full file name of the device list file to export.

*strConverter*
:   Converter long name, see [XPamExportXml](XPamExportXml.html) converters

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for exporting a device list could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export of a device list. Please refer to the exception message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidConverter](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidConverter.html) | Thrown when given parameter  `strConverter`  isn't valid converter or such conversion dosesn't exist at all. |
