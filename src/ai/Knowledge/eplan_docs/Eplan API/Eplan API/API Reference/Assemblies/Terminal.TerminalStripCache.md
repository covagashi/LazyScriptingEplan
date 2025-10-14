# Terminal.TerminalStripCache

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache.html

---

This class is used to enhance performance when getting sub-terminals of multi-level terminals. In order to enhance performance, create an object of this class before accessing sub-terminals of subsequent multi-level terminals and delete it afterwards.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.EObjects.Terminal.TerminalStripCache**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public sealed class Terminal.TerminalStripCache
```
```

```
```
public ref class Terminal.TerminalStripCache sealed
```
```

Example

Example of usage

- [C#](#i-tab-content-673b2cce-56a0-42ed-85bc-902d12f9e4e4)

```
Terminal[] oTerminals = new DMObjectsFinder(m_DistributedTerminalsProject).GetTerminals(null);
using (Terminal.TerminalStripCache oCache = new Terminal.TerminalStripCache())
{
    foreach (Terminal oTerminal in oTerminals)
    {
        StorableObject oParent = oTerminal.ParentFunction;
    }
}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Terminal.TerminalStripCache Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache~_ctor.html) | Constructor |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache~Dispose().html) | Deterministic finalizer |

[Top](#top)




See Also

#### Reference

[Terminal.TerminalStripCache Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache_members.html)
  
[Eplan.EplApi.DataModel.EObjects Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects_namespace.html)