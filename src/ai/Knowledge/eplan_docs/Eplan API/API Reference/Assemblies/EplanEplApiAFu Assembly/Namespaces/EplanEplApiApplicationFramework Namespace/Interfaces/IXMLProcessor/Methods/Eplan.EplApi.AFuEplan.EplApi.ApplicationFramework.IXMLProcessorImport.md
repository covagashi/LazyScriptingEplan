Conversion from sImportFile to sXmlFile. sXmlFile might be passed as "". In this case, the converter must set a file name. EContext may point to an EProgress object to support a progress bar. Returns true if successful.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
bool Import( 
   string strInputFile,
   string strXmlFile,
   Context oContext
)
```
```

```
```
bool Import( 
   String^ strInputFile,
   String^ strXmlFile,
   Context^ oContext
)
```
```

#### Parameters

*strInputFile*
:   Input file

*strXmlFile*
:   Output file

*oContext*
:   Context with parameters



See Also

#### Reference

[IXMLProcessor Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor.html)
  
[IXMLProcessor Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor_members.html)