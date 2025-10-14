# SetPropertyEntry Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~SetPropertyEntry.html

---

Sets a value or variable on a property of an object referenced by a Placeholder3D. The reference of the object will be added to the Placeholder3D if necessary.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void SetPropertyEntry( 
   Placement3D oObject,
   AnyPropertyId oProperty,
   MultiLangString strValue
)
```
```

```
```
public:
virtual void SetPropertyEntry( 
   Placement3D^ oObject,
   AnyPropertyId^ oProperty,
   MultiLangString^ strValue
)
```
```

#### Parameters

*oObject*
:   Object on which the property will be set.

*oProperty*
:   Property

*strValue*
:   Value of the property



See Also

#### Reference

[PlaceHolder3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)
  
[PlaceHolder3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D_members.html)