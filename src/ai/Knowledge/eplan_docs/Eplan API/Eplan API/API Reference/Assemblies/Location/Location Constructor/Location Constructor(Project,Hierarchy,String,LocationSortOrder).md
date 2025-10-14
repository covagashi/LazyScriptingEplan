# Location Constructor(Project,Hierarchy,String,LocationSortOrder)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location~_ctor(Project,Hierarchy,String,LocationSortOrder).html

---

Constructor. Creates a Location and calls `Create` method.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Location( 
   Project oProject,
   Project.Hierarchy eHierarchy,
   string strProps,
   Project.LocationSortOrder eSort
)
```
```

```
```
public:
Location( 
   Project^ oProject,
   Project.Hierarchy eHierarchy,
   String^ strProps,
   Project.LocationSortOrder eSort
)
```
```

#### Parameters

*oProject*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the location will be created.

*eHierarchy*
:   Hierarchy identifier

*strProps*
:   Location name

*eSort*
:   Sort order - determines the position of created location.



See Also

#### Reference

[Location Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location.html)
  
[Location Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location~_ctor.html)