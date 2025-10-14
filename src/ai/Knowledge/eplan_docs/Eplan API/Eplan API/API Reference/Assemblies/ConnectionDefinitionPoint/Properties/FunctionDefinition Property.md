# FunctionDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~FunctionDefinition.html

---

Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Function.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override FunctionDefinition FunctionDefinition {get; set;}
```
```

```
```
public:
property FunctionDefinition^ FunctionDefinition {
   FunctionDefinition^ get() override;
   void set (    FunctionDefinition^ value) override;
}
```
```

#### Property Value

Function's [Function.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) or NULL if Function doesn't have FunctionDefinition.



See Also

#### Reference

[ConnectionDefinitionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint.html)
  
[ConnectionDefinitionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint_members.html)
  
[FunctionDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html)