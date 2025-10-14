# Location Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant~Location.html

---

Get or set the placement's location.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override PointD Location {get; set;}
```
```

```
```
public:
property PointD Location {
   PointD get() override;
   void set (    PointD value) override;
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. For example it is thrown when this property is called on [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) objects. |

Remarks

This property doesn't make sense for class "SymbolVariant". It always throws [Eplan.EplApi.DataModel.ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant".



See Also

#### Reference

[SymbolVariant Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html)
  
[SymbolVariant Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant_members.html)