# GetObjectsFromNavigatorList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetObjectsFromNavigatorList.html

---

Returns all items from the list tab of a navigator.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public StorableObject[] GetObjectsFromNavigatorList( 
   DMObjectsFinder.Enums.Navigators navigator,
   string strFilterScheme
)
```
```

```
```
public:
array<StorableObject^>^ GetObjectsFromNavigatorList( 
   DMObjectsFinder.Enums.Navigators navigator,
   String^ strFilterScheme
)
```
```

#### Parameters

*navigator*
:   Navigator

*strFilterScheme*
:   Filter scheme of a navigator

#### Return Value

\* If the scheme-name is empty, the current filter scheme will be used. \* If the scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.



See Also

#### Reference

[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[DMObjectsFinder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder_members.html)