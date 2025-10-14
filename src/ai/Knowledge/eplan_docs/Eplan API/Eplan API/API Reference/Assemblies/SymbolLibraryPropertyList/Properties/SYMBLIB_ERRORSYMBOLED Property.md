# SYMBLIB_ERRORSYMBOLED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_ERRORSYMBOLED(Int32).html

---

Error (symbol editor) # 15201.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMBLIB_ERRORSYMBOLED( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ SYMBLIB_ERRORSYMBOLED {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Shows whether a problem occurred during the symbol libraries data transfer that can be solved in the symbol editor. Max. of 1,024 are recorded.



See Also

#### Reference

[SymbolLibraryPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html)
  
[SymbolLibraryPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_ERRORSYMBOLED.html)