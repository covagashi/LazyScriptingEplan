# AddLayer(String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~AddLayer(String,MultiLangString).html

---

Creates new layer with specified name and description. Note: Layer name must be unique in the table.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public GraphicalLayer AddLayer( 
   string sName,
   MultiLangString mlsDescription
)
```
```

```
```
public:
GraphicalLayer^ AddLayer( 
   String^ sName,
   MultiLangString^ mlsDescription
)
```
```

#### Parameters

*sName*
:   New layer's name

*mlsDescription*
:   New layer's description

#### Return Value

If succeeded returns newly created GraphicalLayer object, otherwise returns null.



See Also

#### Reference

[GraphicalLayerTable Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.html)
  
[GraphicalLayerTable Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~AddLayer.html)
  
[GraphicalLayer Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html)