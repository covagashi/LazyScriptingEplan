# CableNameParts Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CableNameParts.html

---

Gets/Sets a cable's name to the connection.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public FunctionBasePropertyList CableNameParts {get; set;}
```
```

```
```
public:
property FunctionBasePropertyList^ CableNameParts {
   FunctionBasePropertyList^ get();
   void set (    FunctionBasePropertyList^ value);
}
```
```

#### Property Value

Name of the cable returned as a FunctionBasePropertyList.

Remarks

By setting an existing cable's name to a connection, the connection is assigned to that cable (i.e. becomes the cable's wire).



See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)