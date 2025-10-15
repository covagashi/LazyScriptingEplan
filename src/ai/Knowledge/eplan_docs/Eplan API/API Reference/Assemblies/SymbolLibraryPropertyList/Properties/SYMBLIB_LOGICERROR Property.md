# SYMBLIB_LOGICERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LOGICERROR(Int32).html

---

Error: Connection point logic # 15104.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMBLIB_LOGICERROR( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ SYMBLIB_LOGICERROR {

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

Indicates whether a problem occurred with any connection point logic during the data transfer of symbol libraries. Max. of 1,024 are recorded.
