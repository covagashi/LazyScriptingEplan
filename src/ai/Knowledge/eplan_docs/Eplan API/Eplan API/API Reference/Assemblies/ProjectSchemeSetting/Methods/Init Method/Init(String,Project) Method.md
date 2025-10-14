# Init(String,Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init(String,Project).html

---

Initializes object with a project settings node path.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void Init( 
   string strScheme,
   Project oProj
)
```
```

```
```
public:
virtual void Init( 
   String^ strScheme,
   Project^ oProj
)
```
```

#### Parameters

*strScheme*
:   Path to the project settings node, for example CableLog.CableAutoSelectionScheme

*oProj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) with scheme.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when scheme with given path is not one of given project schemes |

Example

Creating a ProjectSchemeSetting object and initializing it with a scheme path

- [C#](#i-tab-content-3f3240ad-242a-4481-94dd-e43d31c3241a)

```
ProjectSchemeSetting oProjectSchemeSetting = new ProjectSchemeSetting();
oProjectSchemeSetting.Init("CableLog.CableAutoSelectionScheme", m_oTestProject);

```

See Also

#### Reference

[ProjectSchemeSetting Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting.html)
  
[ProjectSchemeSetting Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init.html)