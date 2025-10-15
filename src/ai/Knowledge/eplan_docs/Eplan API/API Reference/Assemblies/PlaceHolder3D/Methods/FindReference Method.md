# FindReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~FindReference.html

---

Finds an object in the list of object referenced by a Placeholder3D.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual int FindReference( 

   Placement3D oObject

)
```
```

```
```
public:

virtual int FindReference( 

   Placement3D^ oObject

)
```
```

#### Parameters

*oObject*
:   The referenced object to search for.

#### Return Value

The index of the reference or -1, if the object was not found.
