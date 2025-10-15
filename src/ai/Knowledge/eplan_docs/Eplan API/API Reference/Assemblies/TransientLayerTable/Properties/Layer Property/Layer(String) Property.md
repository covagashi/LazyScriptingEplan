# Layer(String) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.TransientLayerTable~Layer(String).html

---

Returns one the project's layer as TransientLayer object. If specified layer not exist, null is returned.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public TransientLayer Layer( 

   string name

) {get;}
```
```

```
```
public:

property TransientLayer^ Layer {

   TransientLayer^ get(String^ name);

}
```
```

#### Parameters

*name*
:   Name of the layer to retrieve
