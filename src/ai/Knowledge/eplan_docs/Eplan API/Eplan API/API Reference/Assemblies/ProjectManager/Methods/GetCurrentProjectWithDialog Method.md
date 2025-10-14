# GetCurrentProjectWithDialog Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetCurrentProjectWithDialog.html

---

Gets current project. If there are more than one project open, then displays a dialog to let user choose a current one.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Project GetCurrentProjectWithDialog()
```
```

```
```
public:
Project^ GetCurrentProjectWithDialog();
```
```

#### Return Value

Project : project object. When there is no projects open or the user clicks "Cancel" in project selection window, return value is `null`.



See Also

#### Reference

[ProjectManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager.html)
  
[ProjectManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_members.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)