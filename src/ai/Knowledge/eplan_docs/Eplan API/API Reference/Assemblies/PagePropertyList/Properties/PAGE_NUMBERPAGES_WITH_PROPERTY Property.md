# PAGE_NUMBERPAGES_WITH_PROPERTY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_NUMBERPAGES_WITH_PROPERTY().html

---

Number of pages per property # 11062.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PAGE_NUMBERPAGES_WITH_PROPERTY {get; set;}
```
```

```
```
public:

property PropertyValue^ PAGE_NUMBERPAGES_WITH_PROPERTY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Indicates the number of pages with a specific property. The property is specified in the "Number of pages / Page name per property" project setting. A report run is used to count the pages with the same value as this property, and the result is written to the "Page names per property" property.
