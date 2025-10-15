# UpdateMainElements(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~UpdateMainElements(Project).html

---

Transfers part references of all the part placements in the project to main functions. Corresponds to the 'Devices -> 2D panel layout -> Navigator -> Update main elements' ribbon item.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Function[] UpdateMainElements( 

   Project prj

)
```
```

```
```
public:

array<Function^>^ UpdateMainElements( 

   Project^ prj

)
```
```

#### Parameters

*prj*
:   A project to update main functions in.

#### Return Value

An array of modified main functions.
