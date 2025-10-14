# CopyTo(Group,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group,Boolean,Boolean).html

---

Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Placement CopyTo( 
   Group destinationGroup,
   bool bMatchLayerNames,
   bool bFixUserDefinedDisplayedProperties
)
```
```

```
```
public:
Placement^ CopyTo( 
   Group^ destinationGroup,
   bool bMatchLayerNames,
   bool bFixUserDefinedDisplayedProperties
)
```
```

#### Parameters

*destinationGroup*
:   Group or Page, where the placement will be inserted.

*bMatchLayerNames*
:   Defines whether a layer should be matched by name.

*bFixUserDefinedDisplayedProperties*
:   Defines whether user-defined property definitions should be matched by identifying name.



See Also

#### Reference

[Placement Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)
  
[Placement Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html)