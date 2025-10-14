# Page Constructor(Project,DocumentType,PagePropertyList)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~_ctor(Project,DocumentType,PagePropertyList).html

---

This constructor call the `Create(...)` method automatically.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Page( 
   Project pProject,
   DocumentTypeManager.DocumentType nType,
   PagePropertyList pNameParts
)
```
```

```
```
public:
Page( 
   Project^ pProject,
   DocumentTypeManager.DocumentType nType,
   PagePropertyList^ pNameParts
)
```
```

#### Parameters

*pProject*


*nType*


*pNameParts*

Remarks

The name passed in the pNameParts parameter is validated whether it is correct and not yet existing in the project. Also if PAGE\_COUNTER property is not specified, it is set to a default value automatically.



See Also

#### Reference

[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)
  
[Page Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~_ctor.html)
  
[Create(Project,DocumentType,PagePropertyList) Method](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Create(Project,DocumentType,PagePropertyList).html)