# Layer(String) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layer(String).html

---

Returns one the project's layer as GraphicalLayer object. If specified layer not exist, null is returned.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public GraphicalLayer Layer( 
   string name
) {get;}
```
```

```
```
public:
property GraphicalLayer^ Layer {
   GraphicalLayer^ get(String^ name);
}
```
```

#### Parameters

*name*
:   Name of the layer to retrieve



See Also

#### Reference

[GraphicalLayerTable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.html)
  
[GraphicalLayerTable Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layer.html)
  
[GraphicalLayer Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html)