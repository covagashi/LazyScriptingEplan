The classes of the Scripting namespace provide the attributes for scripts.

Classes

|  | Class | Description |
| --- | --- | --- |
| Class | [DeclareAction](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareAction.html) | Attribute used to mark a method of a class in a [Scripts](Scripts.html) so that this method will be registered as an **Eplan.EplApi.Scripting.Action** in the system. If a method, which is marked by the DeclareAction attribute has string parameters, these \parameters will be recognized as parameters of the Action. |
| Class | [DeclareEventHandler](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareEventHandler.html) | When a script function is to respond to events in the system, the function has to be marked with this attribute. |
| Class | [DeclareMenu](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareMenu.html) | Declares a function that adds only context menu items. |
| Class | [DeclareRegister](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareRegister.html) | When a new script is loaded in P8, this function is called. |
| Class | [DeclareUnregister](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.DeclareUnregister.html) | When a new script is unloaded from P8, this function is called before removing it. |
| Class | [Start](Eplan.EplApi.AFu~Eplan.EplApi.Scripting.Start.html) | Used to mark a function of a class in a [Scripts](Scripts.html). Once the script is run, this function is called. This function may also have [SimpleScriptWithParameters](SimpleScriptWithParameters.html). |

