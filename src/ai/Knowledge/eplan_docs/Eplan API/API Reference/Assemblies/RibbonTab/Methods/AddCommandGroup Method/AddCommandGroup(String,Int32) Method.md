# AddCommandGroup(String,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonTab~AddCommandGroup(String,Int32).html

---

Adds new command group to existing ribbon tab

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public RibbonCommandGroup AddCommandGroup( 

   string name,

   int index

)
```
```

```
```
public:

RibbonCommandGroup^ AddCommandGroup( 

   String^ name,

   int index

)
```
```

#### Parameters

*name*
:   Name of the new command group

*index*
:   Position of a new command group (0-based)

#### Return Value

Created command group or null if it wasn't possible
