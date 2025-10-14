This class implements the standard EPLAN decider dialog.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Decider**

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public class Decider
```
```

```
```
public ref class Decider
```
```

Example

Example of using Decider class:

* [c#](#i-tab-content-4e39bc0f-70e1-49f0-8a40-08762d250e2b)

```
Decider eDecision = new Decider();
EnumDecisionReturn eAnswer = eDecision.Decide(eOkCancelDecision, "Show some dialog text", "Eplan Decider", eOK, eOK);
if (eAnswer == eOK)
{
    // Do your work
}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Decider Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~_ctor.html) | Create a new Decider Object. |






Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Decide](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Decide.html) | Overloaded. Decide shows a list select dialog. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Dispose().html) | Destructor for deterministic finalization of Decider object. |

