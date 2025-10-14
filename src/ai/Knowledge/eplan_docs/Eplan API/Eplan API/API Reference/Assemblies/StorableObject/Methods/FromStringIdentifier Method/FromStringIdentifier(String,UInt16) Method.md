# FromStringIdentifier(String,UInt16) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~FromStringIdentifier(String,UInt16).html

---

Returns this object created from the string identifier

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static StorableObject FromStringIdentifier( 
   string strObject,
   ushort nId
)
```
```

```
```
public:
static StorableObject^ FromStringIdentifier( 
   String^ strObject,
   ushort nId
)
```
```

#### Parameters

*strObject*
:   The string identifier for the object. This string has to be created with the ToString() function.

*nId*
:   The database id the object belongs to. The database id can change when the project is closed and opened again.

#### Return Value

The storable object

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown when the string is not in the correct format |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the object is invalid. |

Remarks

The string is valid during runtime only. When the project the object belongs to is closed, the string gets invalid.



See Also

#### Reference

[StorableObject Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)
  
[StorableObject Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~FromStringIdentifier.html)