# SYMB_INTRINSICALLYSAFE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_INTRINSICALLYSAFE().html

---

Intrinsically safe # 16019.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMB_INTRINSICALLYSAFE {get; set;}
```
```

```
```
public:
property PropertyValue^ SYMB_INTRINSICALLYSAFE {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether an intrinsically safe function is generated when using the symbol:

0 = Not defined (the "Intrinsically safe" property is not observed when placing and replacing a symbol).

1 =Yes (an intrinsically safe function is generated when placing and replacing a symbol for this symbol).

2 = No (a function that is not intrinsically safe is generated when placing and replacing a symbol for this symbol).

The visibility of the property depends on the type of symbol.



See Also

#### Reference

[SymbolPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList.html)
  
[SymbolPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_INTRINSICALLYSAFE.html)