This namespace provides all necessary functionality to integrate API add-ins into EPLAN, to react on events and to work with actions.

Classes

|  | Class | Description |
| --- | --- | --- |
| Class | [Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) | An action performs a task in the system. It is usually called via ribbon items or the [CallingActions](CallingActions.html). \Parameters can be passed to the action in a context class, and return values can be obtained with this parameter. Actions are implemented in an add-in by deriving a class from [IEplAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html). |
| Class | [ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html) | This is the ActionCallingContext class used to pass parameters to an action and to receive return values of the action. |
| Class | [ActionManager](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionManager.html) | Class for retrieving Action objects |
| Class | [ActionParameterProperties](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionParameterProperties.html) | Description of a parameter that can be passed to an ActionCallingContext. This class only serves for documentation purposes. |
| Class | [ActionProperties](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionProperties.html) | This class returns a description text and a list of the parameters that can be passed as context parameters. |
| Class | [CommandLineInterpreter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html) | Class for executing commands in command-line style. |
| Class | [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html) | Base class to handle events. |
| Class | [EventHandlerWrapper](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper.html) | Event handler to process EPLAN events in a remoting client. It is not possible to directly use the [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html) in a remoting client! |
| Class | [EventManager](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventManager.html) | Class for sending events. |
| Class | [EventParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventParameter.html) | Base class for event parameters |
| Class | [EventParameterString](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventParameterString.html) | Event parameter of the System::String data type |
| Class | [License](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License.html) | Class for querying Eplan licensing options ([LicenseOptions](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.LicenseOptions.html)). |
| Class | [QuietModeStep](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.QuietModeStep.html) | Allows setting quiet mode for a part of code |
| Class | [UserRights](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights.html) | Class for checking execute permissions. In the rights management module, you can assign execute permissions to individual actions. These execute permissions are also assigned to specific users. As a result, the rights management system can decide whether the logged-on user has the right to perform a specific action. The rights management system can be completely disabled [CheckUserRights](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckUserRights.html), or it can be set to a specific operating mode (logging on with the current windows user). However, this operating mode cannot be queried or set via API. |

Interfaces

|  | Interface | Description |
| --- | --- | --- |
| Interface | [IActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IActionCallingContext.html) | Interface class for the [ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html) class. Can be used instead of the class in function parameters. |
| Interface | [ICommandLineInterpreter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ICommandLineInterpreter.html) | For internal use only. A fixed interface ID is specified which is used to generate this interface in W3u.exe. This ID is specified in the source code and cannot be changed. |
| Interface | [IEplAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html) | Interface declaration for an action. When an action is to be registered for an add-in (an assembly) in the system, this interface must be implemented by a class of the add-in. |
| Interface | [IEplActionChecked](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionChecked.html) | Interface to switch the status on / off of an Action. If this interface is not used, the Action is off by default. If you implement this interface in an action class, you can set the state of the respective Action to on. If 0, unchecks; if 1, checks; and if 2, sets indeterminate. |
| Interface | [IEplActionEnable](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionEnable.html) | Interface to enable or disable an Action. If this interface is not used, the Action is enabled by default. If you implement this interface in an action class, you can set the respective Action to disabled. If a ribbon item points to this Action, they will be also disabled (grayed out). |
| Interface | [IEplAddIn](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn.html) | Interface declaration for an EPLAN add-in. If an assembly is to be loaded as an EPLAN add-in, exactly one class of the assembly must implement this interface. |
| Interface | [IEplAddInShadowCopy](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy.html) | Provides a mechanism for framework to pass information about original location of the add-in assembly. |
| Interface | [IEplanEvents](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEvents.html) | Declaration of the interface for EPLAN events. |
| Interface | [IEplanEventsWrapper](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplanEventsWrapper.html) | For internal use only. |
| Interface | [IEventParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEventParameter.html) | Base interface declaration for event parameters |
| Interface | [IExtendedProcessor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor.html) | Interface for implementing an extended processor in connection with the IXMLProcessor. |
| Interface | [IInterface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface.html) | A type implementing this interface can be registered as an EPLAN interface. |
| Interface | [IOptions](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IOptions.html) | If a class implements this interface, a settings dialog can be assigned to the XML processor. |
| Interface | [IXMLProcessor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor.html) | Interface for implementing an XML processor. |

Delegates

|  | Delegate | Description |
| --- | --- | --- |
| Delegate | [EventHandlerFunction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerFunction.html) | Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html). |
| Delegate | [EventHandlerNameFunction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerNameFunction.html) | Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html). |
| Delegate | [EventHandlerNameFunctionResult](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerNameFunctionResult.html) | Functions of this type can be registered as event handlers in the class [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html). |

Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Enumeration | [LicenseOptions](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.LicenseOptions.html) | License options provided by the Eplan licensing system. |
| Enumeration | [LicenseType](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.LicenseType.html) | License type: local, network (remote) or borrowed |
| Enumeration | [QuietModes](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.QuietModes.html) | Quiet modes |

