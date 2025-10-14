# ProjectDirectoryPath Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectDirectoryPath.html

---

Project's property which return full project's directory name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string ProjectDirectoryPath {get;}
```
```

```
```
public:
property String^ ProjectDirectoryPath {
   String^ get();
}
```
```

#### Property Value

string : project's directory path for example "C:\\EPLAN\\PROJECTS\\USER\\EPLAN\_Sample\_Project.edb"

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |



See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)