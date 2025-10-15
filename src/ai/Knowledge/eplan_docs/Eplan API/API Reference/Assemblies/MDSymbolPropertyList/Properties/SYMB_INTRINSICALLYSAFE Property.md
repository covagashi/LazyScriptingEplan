# SYMB_INTRINSICALLYSAFE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_INTRINSICALLYSAFE().html

---

Intrinsically safe # 16019.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue SYMB_INTRINSICALLYSAFE {get; set;}
```
```

```
```
public:

property MDPropertyValue^ SYMB_INTRINSICALLYSAFE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

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
