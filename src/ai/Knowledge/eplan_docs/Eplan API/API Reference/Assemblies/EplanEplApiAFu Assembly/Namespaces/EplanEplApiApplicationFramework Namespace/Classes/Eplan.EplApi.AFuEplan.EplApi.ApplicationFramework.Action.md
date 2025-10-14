An action performs a task in the system. It is usually called via ribbon items or the [CallingActions](CallingActions.html). \Parameters can be passed to the action in a context class, and return values can be obtained with this parameter. Actions are implemented in an add-in by deriving a class from [IEplAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.Action**

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public class Action
```
```

```
```
public ref class Action
```
```

Remarks

Actions are registered under a name [Name](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Name.html) in the system. Using this name, you can find an action and call its execution function [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Execute.html). Please mind, that Microsoft.Net framework 3.5 contains a class System.Action. If you include the namespace Eplan.EplApi.ApplicationFramework in your code file by e.g. a using statement without the use of an alias, you might get a compiler error like: "'Action' is an ambiguous reference between 'System.Action' and 'Eplan.EplApi.ApplicationFramework.Action'". Action names with . are not allowed.



Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Action Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~_ctor(AfAction).html) | For internal use only. |





Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActionProperties](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~ActionProperties.html) | Descriptive data for this action. |
| Public Property | [ModuleName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~ModuleName.html) | Name of the module in which this action is implemented. |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Name.html) | Name used to identify this action in the system. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Execute.html) | Performs the actual action. |
| Public Method | [GetChecked](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetChecked.html) | Returns 'checked' state of an action |
| Public Method | [GetEnabled](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetEnabled.html) | Returns whether an action is enabled |


