# ExportDatabaseTexts Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ExportDatabaseTexts.html

---

Exporting text from translation database

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ExportDatabaseTexts( 

   string strFilename,

   string strConverter

)
```
```

```
```
public:

bool ExportDatabaseTexts( 

   String^ strFilename,

   String^ strConverter

)
```
```

#### Parameters

*strFilename*
:   Full file name.

*strConverter*
:   Converter long name, see [XPamExportXml](XPamExportXml.html) converters

#### Return Value

true, in case of no error.
