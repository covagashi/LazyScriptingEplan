Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public void GetLicenseModules( 
   ref Dictionary<LicenseOptions,bool> LicenseModulesDic
)
```
```

```
```
public:
void GetLicenseModules( 
   Dictionary<LicenseOptions,bool>^% LicenseModulesDic
)
```
```

#### Parameters

*LicenseModulesDic*
:   A Dictionary of license modules (output parameter).

Remarks

After executing this method, the LicenseModulesDic parameter contains a dictionary of license modules. The key is the license option of the module, the value is the state whether the module license is available or not.

