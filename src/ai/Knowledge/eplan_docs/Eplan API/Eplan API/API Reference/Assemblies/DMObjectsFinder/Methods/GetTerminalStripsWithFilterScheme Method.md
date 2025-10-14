# GetTerminalStripsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetTerminalStripsWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) matching given filter from terminals-navigator.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public TerminalStrip[] GetTerminalStripsWithFilterScheme( 
   string strFilterScheme
)
```
```

```
```
public:
array<TerminalStrip^>^ GetTerminalStripsWithFilterScheme( 
   String^ strFilterScheme
)
```
```

#### Parameters

*strFilterScheme*
:   Scheme-name of filter terminals-navigator

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |

Remarks

\* If scheme-name is empty, the current filter scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.



See Also

#### Reference

[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[DMObjectsFinder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder_members.html)
  
[TerminalStrip Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)