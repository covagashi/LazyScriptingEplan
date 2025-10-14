# LOCATION_NAMEPART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_NAMEPART(Int32).html

---

Structure identifier: superior name component # 1010.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue LOCATION_NAMEPART( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ LOCATION_NAMEPART {
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

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.

Outputs the xth name component of a structure identifier using the index.

Example: For a structure identifier in the form of "=A.B.C.D" the index 3 returns the value "C".



See Also

#### Reference

[LocationPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList.html)
  
[LocationPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_NAMEPART.html)