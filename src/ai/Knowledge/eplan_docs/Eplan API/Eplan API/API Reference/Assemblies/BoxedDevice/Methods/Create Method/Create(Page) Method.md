# Create(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice~Create(Page).html

---

Creates a new BoxedDevice.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 
   Page page
)
```
```

```
```
public:
void Create( 
   Page^ page
)
```
```

#### Parameters

*page*
:   [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) on which the BoxedDevice will be located.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a BoxedDevice cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
| [IncorrectObjectTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectObjectTypeException.html) | Thrown when function is invoked with object of higher class. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |



See Also

#### Reference

[BoxedDevice Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)
  
[BoxedDevice Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice~Create.html)
  
[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)