# UpgradeProjectDatabase(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~UpgradeProjectDatabase(String,String).html

---

Upgrades project. You can check if project need to be upgrade by GetProjectDataCompatibility.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool UpgradeProjectDatabase( 
   string projectPath,
   string newProjectPath
)
```
```

```
```
public:
bool UpgradeProjectDatabase( 
   String^ projectPath,
   String^ newProjectPath
)
```
```

#### Parameters

*projectPath*
:   Path to old .elk project file.

*newProjectPath*
:   Path where upgraded project will be written.

#### Return Value

Function returns value about success.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project  `projectPath`  doesn't exist. |
| [System.ArgumentNullException](#) | Thrown when `projectPath` or  `newProjectPath`  is `null`. |

Remarks

Upgrading project invalidates Project objects having projectPath path.



See Also

#### Reference

[ProjectManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager.html)
  
[ProjectManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~UpgradeProjectDatabase.html)