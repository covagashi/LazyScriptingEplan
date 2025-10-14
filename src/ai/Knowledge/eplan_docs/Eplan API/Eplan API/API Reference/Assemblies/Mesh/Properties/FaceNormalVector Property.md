# FaceNormalVector Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh~FaceNormalVector.html

---

Returns normal vector for face with a given id.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public ValueType FaceNormalVector( 
   uint id
) {get;}
```
```

```
```
public:
property ValueType^ FaceNormalVector {
   ValueType^ get(uint id);
}
```
```

#### Parameters

*id*
:   Face identifier. Valid values are from 0 to FaceCount-1.

#### Property Value

Normal vector for face with a given id.



See Also

#### Reference

[Mesh Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh.html)
  
[Mesh Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh_members.html)