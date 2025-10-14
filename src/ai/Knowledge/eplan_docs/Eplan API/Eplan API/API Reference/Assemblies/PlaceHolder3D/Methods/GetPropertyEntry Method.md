# GetPropertyEntry Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~GetPropertyEntry.html

---

Gets a value or variable on a property of an object referenced by a Placeholder3D.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual MultiLangString GetPropertyEntry( 
   Placement3D oObject,
   AnyPropertyId oProperty
)
```
```

```
```
public:
virtual MultiLangString^ GetPropertyEntry( 
   Placement3D^ oObject,
   AnyPropertyId^ oProperty
)
```
```

#### Parameters

*oObject*
:   Object from which property will be read

*oProperty*
:   The property.

#### Return Value

Value of the variable.

Remarks

If you want to get the text content of a text object, oProperty must have the property id 0.



See Also

#### Reference

[PlaceHolder3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)
  
[PlaceHolder3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D_members.html)