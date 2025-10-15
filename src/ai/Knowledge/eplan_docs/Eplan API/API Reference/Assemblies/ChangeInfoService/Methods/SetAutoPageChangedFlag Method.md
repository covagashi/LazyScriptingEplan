# SetAutoPageChangedFlag Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetAutoPageChangedFlag.html

---

Activate or deactivate AUTOPAGECHANGED change info handling. Helper will switch mode automatically back due to destruction.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetAutoPageChangedFlag( 

   bool bAutoPageChangedFlag,

   ChangeInfoService.ChangeInfoServiceHelper pHelper

)
```
```

```
```
public:

void SetAutoPageChangedFlag( 

   bool bAutoPageChangedFlag,

   ChangeInfoService.ChangeInfoServiceHelper^ pHelper

)
```
```

#### Parameters

*bAutoPageChangedFlag*
:   If true, AUTOPAGECHANGED change info handling is activated.

*pHelper*
:   Object which will switch mode back due to destruction. Can be null value.
