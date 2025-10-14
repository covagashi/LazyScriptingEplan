# FacePoints Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh~FacePoints.html

---

Returns points for a given id of face.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PointD3D[] FacePoints( 
   uint id
) {get;}
```
```

```
```
public:
property array<PointD3D>^ FacePoints {
   array<PointD3D>^ get(uint id);
}
```
```

#### Parameters

*id*
:   Face identifier. Valid values are from 0 to FaceCount-1.

#### Property Value

Points for a given id of face.



See Also

#### Reference

[Mesh Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh.html)
  
[Mesh Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh_members.html)