This namespace exposes base functionality of EPLAN, like a base class for exceptions, and classes to access the EPLAN settings.

Classes

|  | Class | Description |
| --- | --- | --- |
| Class | [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception class derived from ApplicationException. This is the base class for the exceptions that might occur in the API. |
| Class | [Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html) | The Context classes are used to pass information about the current state of the environment as well as generic parameters to objects that can be registered such as actions, dialogs, etc. |
| Class | [ContextParameterBlock](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ContextParameterBlock.html) | A Parameter block for a context. This parameterblock can have System::Object^ as parameters. This block can be used to add objects to a context and work with this objects p.e. inside an action. |
| Class | [Decider](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html) | This class implements the standard EPLAN decider dialog. |
| Class | [EplAssert](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplAssert.html) | The EplAssert class. When the advaced mode is activated in ELogFileConfigTool, Asserts are written to the epllog.txt Its also possible to activate a debugger break. Set the registry value User / Software / Eplan / Eplan W3 / Assert / BreakOnAssert to true, and the debugger will stop at a failed assert. |
| Class | [EplTrace](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace.html) | Trace the output to the EplLog.txt file. This Trace class works in debug and release mode, while the trace listener works only in debug mode. Traces are written when the registry key HKCU / Software / Eplan / Eplan W3 / Trace / \-ModuleName- is found. |
| Class | [FileSelectDecisionContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext.html) | This class can be used for an standard eplan decider |
| Class | [ISOCode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISOCode.html) | Class for managing language codes (abbreviations). [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) can handle these languages. |
| Class | [LanguageList](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LanguageList.html) | Class for managing a list of languages. |
| Class | [Languages](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Languages.html) | Class for language information. |
| Class | [ListSelectDecisionContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ListSelectDecisionContext.html) | This class can be used for a standard Eplan decider |
| Class | [LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) | Exception class that signals locking errors in DataModel. |
| Class | [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) | This class can save strings in various languages at the same time. Each string can be added, queried, and deleted individually. |
| Class | [ParserParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ParserParameter.html) | Parameter Class for the usage with UnitParser. Configure the unit and the look of the Parser result. |
| Class | [PathMap](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PathMap.html) | This class enables you access to the functions used for processing strings that could contain EPLAN path variables. |
| Class | [Progress](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress.html) | This class enables you to access the functions of the progress bar in EPLAN. |
| Class | [ProgressFactory](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ProgressFactory.html) | This class can be used for OfflineApplications. With RegisterProgress a progress can be installed in Eplan. UnregisterProgress removes this progress from Eplan again. |
| Class | [Range](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Range.html) | Range of setting values |
| Class | [SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html) | Class for editing settings that are grouped into schemes |
| Class | [SettingNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html) | Allows access to settings and relative access to setting-nodes. A setting key consists of a number of sections separated by '.' Each section except the last one is called a setting-node. Setting-nodes and settings together build the settings tree. The settings are the leaves of this tree. The SettingNode class helps iterating trough the nodes and e.g. gives you the possibility to delete a node completely. |
| Class | [Settings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html) | Settings are used to save values of variables beyond the runtime of the program and to make them available again the next time program is run (similar to the Windows registry). A setting has a unique identifier in the system. A value or a list of values can be saved to a setting. It is possible to group settings into structures [SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html). |
| Class | [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) | Class that represents the system-wide message tree. The collection contains the system messages as BaseException objects. |
| Class | [SysMessagesEnumerator](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesEnumerator.html) | supports a simple iteration over [SysMessagesCollection](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SysMessagesCollection.html) |
| Class | [TraceListener](Eplan.EplApi.Baseu~Eplan.EplApi.Base.TraceListener.html) | Output of trace messages to the EPLAN system message management (incl. EPLAN log file) |
| Class | [UnitParser](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser.html) | The UnitParser class. Here it is possible to read the unit from a string and convert it in other units (of the same unit group) |

Interfaces

|  | Interface | Description |
| --- | --- | --- |
| Interface | [IContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext.html) | IContext is an abstract interface for Context classes. |
| Interface | [IEplProgress](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IEplProgress.html) | Interface declaration for a progress. When a progress is to be registered for an add-in (an assembly) in the system, this interface must be implemented by a class of the add-in. |
| Interface | [ISettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings.html) | The common interface to P8 settings. |

Structures

|  | Structure | Description |
| --- | --- | --- |
| Structure | [PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) | This class represents a set of coordinates in EPLAN. |
| Structure | [PointD3D](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD3D.html) | This class represents a set of 3D coordinates in EPLAN. |
| Structure | [RectangleD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.RectangleD.html) | This class specifies an area in a coordinate space. |

Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Enumeration | [EnumDecisionIcon](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EnumDecisionIcon.html) | Used by the [Decider](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html), to determine which icon is to be shown. |
| Enumeration | [EnumDecisionReturn](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EnumDecisionReturn.html) | This enum is returned by the [Decider](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html) method. |
| Enumeration | [EnumDecisionType](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EnumDecisionType.html) | The type one setting can hold data in. |
| Enumeration | [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html) | Creation flag |
| Enumeration | [ISettings.SettingType](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+SettingType.html) | The type one setting can hold data in. |
| Enumeration | [ISOCode.Language](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISOCode+Language.html) | [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) can handle these languages. |
| Enumeration | [MessageLevel](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MessageLevel.html) | Severity of the error |
| Enumeration | [Unit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Unit.html) | A unit. Every unit enum starts with the group name. |
| Enumeration | [UnitGroup](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitGroup.html) | The group of one unit. Conversion is only possible inside groups |

See Also

#### Reference

[Eplan.EplApi.Baseu Assembly](Eplan.EplApi.Baseu.html)