# TryParseIdentifier(String,StorableObject) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TryParseIdentifier(String,StorableObject).html

---

Returns this object created from the string identifier

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static bool TryParseIdentifier( 
   string strObject,
   ref StorableObject resultObj
)
```
```

```
```
public:
static bool TryParseIdentifier( 
   String^ strObject,
   StorableObject^% resultObj
)
```
```

#### Parameters

*strObject*
:   The string identifier for the object. This string has to be created with the ToString() function.

*resultObj*
:   The storable object

#### Return Value

true when the object was created successfully

Remarks

The string is valid during runtime only. When the project the object belongs to is closed, the string gets invalid.



See Also

#### Reference

[StorableObject Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)
  
[StorableObject Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TryParseIdentifier.html)