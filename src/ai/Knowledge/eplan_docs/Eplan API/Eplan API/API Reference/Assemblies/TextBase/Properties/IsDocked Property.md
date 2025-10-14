# IsDocked Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~IsDocked.html

---

Gets/Sets a value that indicates whether the text is docked or not. Setting IsDocked to true is possible only on PropertyPlacement object which Parent is a SymbolReference object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsDocked {get; set;}
```
```

```
```
public:
property bool IsDocked {
   bool get();
   void set (    bool value);
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when property cannot be set. |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when the PropertyPlacement object has not been initialized. |
| [System.InvalidOperationException](#) | Thrown when property cannot be set i.e. it is not possible to dock first PropertyPlacement. |



See Also

#### Reference

[TextBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase.html)
  
[TextBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase_members.html)
  
[DockText Method](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~DockText.html)
  
[UndockText Method](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~UndockText.html)