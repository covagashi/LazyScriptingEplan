# Paths Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~Paths.html

---

Returns [PathInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo.html) object. It is intended to provide information about default Eplan Platform paths.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PathInfo Paths {get;}
```
```

```
```
public:

property PathInfo^ Paths {

   PathInfo^ get();

}
```
```

#### Property Value

New [PathInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo.html) object.

Example

- [C#](#i-tab-content-c69c70ac-f068-472d-8095-97908416df60)

```
string defaultProjectPath = new ProjectManager().Paths.Projects;

string defaultTemplatesPath = new ProjectManager().Paths.Templates;
```
