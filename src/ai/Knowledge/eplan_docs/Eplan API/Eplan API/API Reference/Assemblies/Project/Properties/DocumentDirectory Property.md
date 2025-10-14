# DocumentDirectory Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DocumentDirectory.html

---

Project's property which return full project documents' directory name

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string DocumentDirectory {get;}
```
```

```
```
public:
property String^ DocumentDirectory {
   String^ get();
}
```
```

#### Property Value

string : project documents' directory path for example "C:\\EPLAN\\PROJECTS\\USER\\EPLAN\_Sample\_Project.edb\\DOC"

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |



See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)