# PAGE_REVISION_LOG_PROJ_REV Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_PROJ_REV(Int32).html

---

Associated project revision (change tracking) # 11075.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PAGE_REVISION_LOG_PROJ_REV( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ PAGE_REVISION_LOG_PROJ_REV {
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

Outputs the internal index value of the associated project revision (from change tracking) on a page; max. 1,000 entries are allowed.



See Also

#### Reference

[PagePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html)
  
[PagePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_REVISION_LOG_PROJ_REV.html)