# PAGE_REVISION_LOG_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_NAME(Int32).html

---

Revision index (change tracking) # 11071.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PAGE_REVISION_LOG_NAME( 

   int index

) {get; set;}
```
```

```
```
public:

property PropertyValue^ PAGE_REVISION_LOG_NAME {

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

Property is indexed. Possible indexes are from 1 to 1000.

Text used to identify change. Existing values can be selected from a list. A max. of 1,000 is allowed.
