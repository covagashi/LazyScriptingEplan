# DeviceTagConfig Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html

---

Predefined property for accessing following project settings: EnableSyntaxCheck, UserCharacters, AllowUserCharacters, AllowedLetters, AllowSpecialCharacters, PlantDesignationNumbersOnly.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Project.DeviceTagSettings DeviceTagConfig {get;}
```
```

```
```
public:
property Project.DeviceTagSettings^ DeviceTagConfig {
   Project.DeviceTagSettings^ get();
}
```
```

#### Property Value

Object of DeviceTagSettings class.

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when project is invalid object. |
| [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when project is not created. |

Remarks

This property might throw exceptions caused by [DeviceTagConfig](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html).

Example

- [C#](#i-tab-content-570eff61-c18d-4bb1-9e4c-caa5b3060c30)

```
using Eplan.EplApi.DataModel;
 Project proj; // = ....
  proj.DeviceTagConfig.EnableSyntaxCheck = true;
  proj.DeviceTagConfig.UserCharacters = @"^";
  proj.DeviceTagConfig.AllowUserCharacters = true;

 // now it is possible to use for example:
 Page page; // = ...
  page.Name = @"=^^^^+^^";
```

See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)
  
[DeviceTagConfig Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html)
  
[Settings Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Settings.html)