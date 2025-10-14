# ExistsProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~ExistsProject.html

---

Check if project placed on given path exist.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ExistsProject( 
   string projectFullPath
)
```
```

```
```
public:
bool ExistsProject( 
   String^ projectFullPath
)
```
```

#### Parameters

*projectFullPath*
:   Full path to project's link file.

#### Return Value

true : project exist

false : can not find project

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `projectFullPath` is `null`. |



See Also

#### Reference

[ProjectManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager.html)
  
[ProjectManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_members.html)