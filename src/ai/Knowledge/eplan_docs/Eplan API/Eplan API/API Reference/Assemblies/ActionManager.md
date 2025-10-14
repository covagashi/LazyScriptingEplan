# ActionManager

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager.html

---

Class for retrieving Action objects

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.ActionManager**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class ActionManager
```
```

```
```
public ref class ActionManager
```
```

Example

- [C#](#i-tab-content-197a471a-3d16-4dba-937e-8d138e13e34d)

```
Action oAction = m_ActionManager.FindAction(null);
Assert.IsNull(oAction);
ActionCallingContext oACC = new ActionCallingContext();
oAction.Execute(oACC);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ActionManager Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~_ctor.html) |  |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [FindAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindAction.html) | Overloaded. This function searches for an action registered in the system. |
| Public Method | [FindBaseAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindBaseAction.html) | This function searches the base action for an existing action the base action has the same name, but a lower ordinal. |
| Public Method | [FindBaseActionFromFunctionAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager~FindBaseActionFromFunctionAction.html) | This function searches the base action for an existing action in scripting. the base action has the same name, but a lower ordinal. |

[Top](#top)




See Also

#### Reference

[ActionManager Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager_members.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)