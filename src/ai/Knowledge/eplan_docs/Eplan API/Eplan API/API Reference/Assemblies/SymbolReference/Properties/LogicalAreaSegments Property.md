# LogicalAreaSegments Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~LogicalAreaSegments.html

---

Gets/Sets an array of segments that the symbol's logical area may consist of.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual SymbolReference.Segment[] LogicalAreaSegments {get; set;}
```
```

```
```
public:
virtual property array<SymbolReference.Segment^>^ LogicalAreaSegments {
   array<SymbolReference.Segment^>^ get();
   void set (    array<SymbolReference.Segment^>^ value);
}
```
```

Remarks

Note: After setting the logical area with the [SetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SetLogicalArea.html) method this property returns an array containing 3 segments (that represent a rectangular area)



See Also

#### Reference

[SymbolReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)
  
[SymbolReference Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference_members.html)