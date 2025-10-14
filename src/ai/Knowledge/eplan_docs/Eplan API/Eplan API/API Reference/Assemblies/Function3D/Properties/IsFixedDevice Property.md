# IsFixedDevice Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~IsFixedDevice.html

---

Set or checks if device of this Function3d is fixed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsFixedDevice {get; set;}
```
```

```
```
public:
property bool IsFixedDevice {
   bool get();
   void set (    bool value);
}
```
```

Remarks

If device is fixed no [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html) can be added/changed/removed from device of this Function3D. The same is with properties FUNC\_ARTICLE\_PARTNR and FUNC\_ARTICLE\_COUNT.



See Also

#### Reference

[Function3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)
  
[Function3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D_members.html)
  
[ArticleReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)