# MacroRepresentationTypeNameFromId Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~MacroRepresentationTypeNameFromId.html

---

Converts macro representation type to a displayed name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static string MacroRepresentationTypeNameFromId( 

   WindowMacro.Enums.RepresentationType nRepType

)
```
```

```
```
public:

static String^ MacroRepresentationTypeNameFromId( 

   WindowMacro.Enums.RepresentationType nRepType

)
```
```

#### Parameters

*nRepType*
:   Input parameter - representation type (as enum)

#### Return Value

Method converts macro representation type to a name visible in the 'Select macro' dialog. Current GUI language is used.
