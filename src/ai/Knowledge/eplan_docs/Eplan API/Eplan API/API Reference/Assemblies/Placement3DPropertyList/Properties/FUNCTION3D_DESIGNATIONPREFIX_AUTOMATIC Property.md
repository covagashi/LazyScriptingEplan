# FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC().html

---

Grouping sign for item designation (automatic) # 36002.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the contents of the "Grouping sign for item designation" property (ID 36012). If no preceding sign is entered for the item, this is defined from the first superior item for which a preceding sign is entered in the "Grouping sign for item designation" property.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC.html)