# AssignedObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~AssignedObjects.html

---

Gets/Sets a list of StorableObject references to a PlaceHolder3D object. The originally assigned references are replaced.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual StorableObject[] AssignedObjects {get; set;}
```
```

```
```
public:
virtual property array<StorableObject^>^ AssignedObjects {
   array<StorableObject^>^ get();
   void set (    array<StorableObject^>^ value);
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |



See Also

#### Reference

[PlaceHolder3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)
  
[PlaceHolder3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D_members.html)