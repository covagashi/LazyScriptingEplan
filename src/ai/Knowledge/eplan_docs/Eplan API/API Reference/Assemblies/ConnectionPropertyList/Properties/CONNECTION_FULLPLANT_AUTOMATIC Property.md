# CONNECTION_FULLPLANT_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_FULLPLANT_AUTOMATIC().html

---

Function designation (automatic) # 31101.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_FULLPLANT_AUTOMATIC {get; set;}
```
```

```
```
public:

property PropertyValue^ CONNECTION_FULLPLANT_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

If a DT is entered on the connection, the corresponding structure identifier is output. Otherwise, the structure identifier from the connection source is output. The source is determined by its position in the schematic and can be exchanged with the target over a connection definition point.
