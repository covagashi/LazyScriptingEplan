Trace the output to the EplLog.txt file. This Trace class works in debug and release mode, while the trace listener works only in debug mode. Traces are written when the registry key HKCU / Software / Eplan / Eplan W3 / Trace / \-ModuleName- is found.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.EplTrace**

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public class EplTrace
```
```

```
```
public ref class EplTrace
```
```

Example

Example of TRACE outputs

* [c#](#i-tab-content-c840c37d-9b0a-4592-9a8a-e2b77ffdbe97)

```
Eplan.EplApi.Base.EplTrace oTrace= new Eplan.EplApi.Base.EplTrace();
oTrace.Trace ("Eplan.EplApi.Base", "Start executing function abc");
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplTrace Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace~_ctor.html) |  |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Trace](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace~Trace.html) | Overloaded. Writes the text to EplLog.txt when Trace is on. |

[Top](#top)




See Also

#### Reference

[EplTrace Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace_members.html)
  
[Eplan.EplApi.Base Namespace](Eplan.EplApi.Baseu~Eplan.EplApi.Base_namespace.html)