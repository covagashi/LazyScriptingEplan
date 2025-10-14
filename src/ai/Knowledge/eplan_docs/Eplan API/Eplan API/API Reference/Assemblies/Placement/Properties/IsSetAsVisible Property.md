# IsSetAsVisible Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html

---

Gets/Sets visibility of the object as set in its properties dialog.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual Placement.Visibility IsSetAsVisible {get; set;}
```
```

```
```
public:
virtual property Placement.Visibility IsSetAsVisible {
   Placement.Visibility get();
   void set (    Placement.Visibility value);
}
```
```

Remarks

This property may return 'Invisible' even if the object is actually visible on the page because of the 'Show invisible elements' setting of GED.



See Also

#### Reference

[Placement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)
  
[Placement Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement_members.html)