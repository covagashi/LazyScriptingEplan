# CreateFromProjectProperties Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~CreateFromProjectProperties.html

---

Creates and insert into page ContextPropertyPlacement which displays project property.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CreateFromProjectProperties( 
   Page oPage,
   PointD oLocation,
   AnyPropertyId oAnyPropertyId
)
```
```

```
```
public:
void CreateFromProjectProperties( 
   Page^ oPage,
   PointD oLocation,
   AnyPropertyId^ oAnyPropertyId
)
```
```

#### Parameters

*oPage*
:   Page on which object will be inserted.

*oLocation*
:   Location in which object will be inserted.

*oAnyPropertyId*
:   Project property which will be displayed.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Throw when DataModel object has already been created and is created again. |
| [System.ArgumentNullException](#) | Thrown when one of parameters is `null`. Check exception message for more details. |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Throw when internally used handle is not valid. |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when ContextPropertyPlacement object cannot be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal problem occurs. Check exception message for more details. |

Example

- [C#](#i-tab-content-3aa5199f-2948-4025-b3a2-a7de14b0588f)

```
ContextPropertyPlacement oContextPropertyPlacement = new ContextPropertyPlacement();
oContextPropertyPlacement.CreateFromProjectProperties(oNewPage, new PointD(100.0, 100.0), m_oTestProject.Properties["EPLAN.Project.UserSupplementaryField1"].Id);

```

See Also

#### Reference

[ContextPropertyPlacement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement.html)
  
[ContextPropertyPlacement Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement_members.html)
  
[CreateFromPageProperties Method](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~CreateFromPageProperties.html)