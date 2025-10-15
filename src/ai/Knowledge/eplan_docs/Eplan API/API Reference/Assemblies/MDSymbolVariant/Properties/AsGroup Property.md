# AsGroup Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolVariant~AsGroup.html

---

The group of the symbol variant. That is needed to add graphical placements.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Group AsGroup {get;}
```
```

```
```
public:

property Group^ AsGroup {

   Group^ get();

}
```
```

#### Property Value

Group of the symbol variant.

Example

- [C#](#i-tab-content-51aef15b-314c-4e1d-b0df-a95059ef0675)

```
MDSymbolVariant symVar = sym.AddSymbolVariant(0);

Group grp = symVar.AsGroup;

Line lin = Line.Create(grp);

lin.StartPoint = new PointD(-50.0, 150.0);

lin.EndPoint = new PointD(-50.0, 50.0);
```
