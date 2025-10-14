# DisplayedProperty Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~DisplayedProperty.html

---

Return [Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) equal to displayed property id.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public AnyPropertyId DisplayedProperty {get; set;}
```
```

```
```
public:
property AnyPropertyId^ DisplayedProperty {
   AnyPropertyId^ get();
   void set (    AnyPropertyId^ value);
}
```
```

#### Property Value

[Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) equal to displayed property id.

Example

- [C#](#i-tab-content-4f721071-5552-4940-b822-a7a195f8d651)

```
PropertyPlacement p1;//a valid PropertyPlacement object
PropertyPlacement p2;//a valid PropertyPlacement object

if (p1.Source == p2.Source)
{
	//two PropertyPlacements show the same property id
}
```

See Also

#### Reference

[PropertyPlacement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)
  
[PropertyPlacement Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement_members.html)