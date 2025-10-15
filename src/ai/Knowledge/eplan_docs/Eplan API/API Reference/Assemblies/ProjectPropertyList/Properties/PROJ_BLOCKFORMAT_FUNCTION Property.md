# PROJ_BLOCKFORMAT_FUNCTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_BLOCKFORMAT_FUNCTION(Int32).html

---

Block property: Format (general devices) # 10600.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PROJ_BLOCKFORMAT_FUNCTION( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ PROJ_BLOCKFORMAT_FUNCTION {

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

Property is indexed. Possible indexes are from 1 to 100.

Predefines which properties are specified in the relevant block property. If you assign a "Block property [n]" to a function and a format is not entered for either the function or the symbol, then the program uses the relevant format property that has been entered for this function category in the project.
