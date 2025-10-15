# GenerateMacrosFromMacroProject(ICollection<StorableObject>,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1382.html

---

Generate macros from collection of objects with macro definition.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void GenerateMacrosFromMacroProject( 

   ICollection<StorableObject> colObjects,

   string strWindowMacroDirectory,

   string strPageMacroDirectory,

   bool bOverwriteExistingMacros

)
```
```

```
```
public:

void GenerateMacrosFromMacroProject( 

   ICollection<StorableObject^>^ colObjects,

   String^ strWindowMacroDirectory,

   String^ strPageMacroDirectory,

   bool bOverwriteExistingMacros

)
```
```

#### Parameters

*colObjects*
:   Collection of objects with macro definition.

*strWindowMacroDirectory*
:   Specifies output directory for window macros. If empty or null default macro directory is used.

*strPageMacroDirectory*
:   Specifies output directory for window macros. If empty or null default macro directory is used.

*bOverwriteExistingMacros*
:   If the output file already exists specifies whether it should be overwritten.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | A parameter was set to a null reference. |
| [System.ArgumentException](#) | Parameters are invalid, e.g. collection of objects is empty. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be exported. |

Example

The following examples shows how to use method GenerateMacrosFromMacroProject.

- [C#](#i-tab-content-3a941529-cac7-48f2-8df6-08080b20838f)

```
List<StorableObject> lObjects = new List<StorableObject>();

lObjects.Add(oTestProject.Pages[0]); //Page with macro box - generates window macro 

lObjects.Add(oTestProject.Pages[3]); //Page with macro definition - generates page macro

lObjects.Add(oTestProject.InstallationSpaces[0]); //InstallationSpace with macro definition - generates window macro                

lObjects.Add(oMacroBox); //MacroBox - generates window macro



// Generate macros to default macros directory    

new Masterdata().GenerateMacrosFromMacroProject(lObjects, null, null, true);



```
