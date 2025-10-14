# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.LockedMountingArea~Create(Page).html

---

Creates the Rectangle object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override void Create( 
   Page page
)
```
```

```
```
public:
void Create( 
   Page^ page
) override
```
```

#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the Line will be placed on.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Rectangle cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Rectangle has already been created. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |



See Also

#### Reference

[LockedMountingArea Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.LockedMountingArea.html)
  
[LockedMountingArea Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.LockedMountingArea_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.LockedMountingArea~Create.html)
  
[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)