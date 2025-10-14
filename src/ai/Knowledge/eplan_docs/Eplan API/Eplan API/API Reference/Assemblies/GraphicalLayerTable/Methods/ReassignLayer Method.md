# ReassignLayer Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~ReassignLayer.html

---

Reassign all elements from `sourceLayer` to `targetLayer`.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ReassignLayer( 
   GraphicalLayer sourceLayer,
   GraphicalLayer targetLayer
)
```
```

```
```
public:
bool ReassignLayer( 
   GraphicalLayer^ sourceLayer,
   GraphicalLayer^ targetLayer
)
```
```

#### Parameters

*sourceLayer*
:   Layer from which objects should be reassigned.

*targetLayer*
:   Layer to which objects shoud be reassigned.

#### Return Value

`true` when reassigned correctly.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |



See Also

#### Reference

[GraphicalLayerTable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.html)
  
[GraphicalLayerTable Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable_members.html)