# Eplan.EplApi.Base Namespace
This namespace exposes base functionality of EPLAN, like a base class for exceptions, and classes to access the EPLAN settings.
Classes
 	Class	Description
Class	BaseException 	Exception class derived from ApplicationException. This is the base class for the exceptions that might occur in the API.
Class	Context 	The Context classes are used to pass information about the current state of the environment as well as generic parameters to objects that can be registered such as actions, dialogs, etc.
Class	ContextParameterBlock 	A Parameter block for a context. This parameterblock can have System::Object^ as parameters. This block can be used to add objects to a context and work with this objects p.e. inside an action.
Class	Decider 	This class implements the standard EPLAN decider dialog.
Class	EplAssert 	The EplAssert class. When the advaced mode is activated in ELogFileConfigTool, Asserts are written to the epllog.txt Its also possible to activate a debugger break. Set the registry value User / Software / Eplan / Eplan W3 / Assert / BreakOnAssert to true, and the debugger will stop at a failed assert.
Class	EplTrace 	Trace the output to the EplLog.txt file. This Trace class works in debug and release mode, while the trace listener works only in debug mode. Traces are written when the registry key HKCU / Software / Eplan / Eplan W3 / Trace / \-ModuleName- is found.
Class	FileSelectDecisionContext 	This class can be used for an standard eplan decider
Class	ISOCode 	Class for managing language codes (abbreviations). MultiLangString can handle these languages.
Class	LanguageList 	Class for managing a list of languages.
Class	Languages 	Class for language information.
Class	ListSelectDecisionContext 	This class can be used for a standard Eplan decider
Class	LockingException 	Exception class that signals locking errors in DataModel.
Class	MultiLangString 	This class can save strings in various languages at the same time. Each string can be added, queried, and deleted individually.
Class	ParserParameter 	Parameter Class for the usage with UnitParser. Configure the unit and the look of the Parser result.
Class	PathMap 	This class enables you access to the functions used for processing strings that could contain EPLAN path variables.
Class	Progress 	This class enables you to access the functions of the progress bar in EPLAN.
Class	ProgressFactory 	This class can be used for OfflineApplications. With RegisterProgress a progress can be installed in Eplan. UnregisterProgress removes this progress from Eplan again.
Class	Range 	Range of setting values
Class	SchemeSetting 	Class for editing settings that are grouped into schemes
Class	SettingNode 	Allows access to settings and relative access to setting-nodes. A setting key consists of a number of sections separated by '.' Each section except the last one is called a setting-node. Setting-nodes and settings together build the settings tree. The settings are the leaves of this tree. The SettingNode class helps iterating trough the nodes and e.g. gives you the possibility to delete a node completely.
Class	Settings 	Settings are used to save values of variables beyond the runtime of the program and to make them available again the next time program is run (similar to the Windows registry). A setting has a unique identifier in the system. A value or a list of values can be saved to a setting. It is possible to group settings into structures SchemeSetting.
Class	SysMessagesCollection 	Class that represents the system-wide message tree. The collection contains the system messages as BaseException objects.
Class	SysMessagesEnumerator 	supports a simple iteration over SysMessagesCollection
Class	TraceListener 	Output of trace messages to the EPLAN system message management (incl. EPLAN log file)
Class	UnitParser 	The UnitParser class. Here it is possible to read the unit from a string and convert it in other units (of the same unit group)
Interfaces
 	Interface	Description
Interface	IContext 	IContext is an abstract interface for Context classes.
Interface	IEplProgress 	Interface declaration for a progress. When a progress is to be registered for an add-in (an assembly) in the system, this interface must be implemented by a class of the add-in.
Interface	ISettings 	The common interface to P8 settings.
Structures
 	Structure	Description
Structure	PointD 	This class represents a set of coordinates in EPLAN.
Structure	PointD3D 	This class represents a set of 3D coordinates in EPLAN.
Structure	RectangleD 	This class specifies an area in a coordinate space.
Enumerations
 	Enumeration	Description
Enumeration	EnumDecisionIcon 	Used by the Decider, to determine which icon is to be shown.
Enumeration	EnumDecisionReturn 	This enum is returned by the Decider method.
Enumeration	EnumDecisionType 	The type one setting can hold data in.
Enumeration	ISettings.CreationFlag 	Creation flag
Enumeration	ISettings.SettingType 	The type one setting can hold data in.
Enumeration	ISOCode.Language 	MultiLangString can handle these languages.
Enumeration	MessageLevel 	Severity of the error
Enumeration	Unit 	A unit. Every unit enum starts with the group name.
Enumeration	UnitGroup 	The group of one unit. Conversion is only possible inside groups

### BaseException Class
Exception class derived from ApplicationException. This is the base class for the exceptions that might occur in the API.
Eplan.EplApi.MasterData.MasterDataException
```csharp    
public class BaseException : System.ApplicationException 
``` 
Public Constructors:
Public Constructor	BaseException Constructor	Overloaded. 
Public Properties:
Public Property	Data	(Inherited from System.Exception)
Public Property	HelpLink	(Inherited from System.Exception)
Public Property	HResult	(Inherited from System.Exception)
Public Property	InnerException	(Inherited from System.Exception)
Public Property	Message	(Inherited from System.Exception)
Public Property	MessageLevel	Returns the level of message as MessageLevel.  
Public Property	NumberOfOccurrences	Returns number of repetitions of consecutive messages with the same text (i.e. error description) which are joined into one item in the system's message tree.  
Public Property	Source	(Inherited from System.Exception)
Public Property	StackTrace	(Inherited from System.Exception)
Public Property	TargetSite	(Inherited from System.Exception)
Public Methods:
Public Method	Dispose	Destructor for deterministic finalization of BaseException object.  
Public Method	FixMessage	Method enters a message in the system-wide message tree.  
Public Method	GetBaseException	(Inherited from System.Exception)
Public Method	GetBookmarkID	Sets a label in the system error message management for getting a section of the 'message tree'  
Public Method	GetMessageIndex	returns the identifying S- number of a system message  
Public Method	GetMessageText	Returns the text of the system message without the index  
Public Method	GetObjectData	(Inherited from System.Exception)
Public Method	GetType	(Inherited from System.Exception)
Public Method	ToString	(Inherited from System.Exception)
### Context Class
The Context classes are used to pass information about the current state of the environment as well as generic parameters to objects that can be registered such as actions, dialogs, etc.
 Eplan.EplApi.EServices.Ged.InteractionContext
```csharp 
public class Context : IContext
```
Public Constructors 
Public Constructor	Context Constructor	Overloaded.   
Public Methods
Public Method	AddParameter	Adds a parameter to the Context.  
Public Method	Dispose	Destructor for deterministic finalization of Context object.  
Public Method	GetContextParameter	Get the Block of Context Parameters of this Context.  
Public Method	GetEContext	For internal use only.  
Public Method	GetParameter	Gets a parameter from the Context.  
Public Method	GetParameterCount	Gets the count of the Parameters in this context  
Public Method	GetParameters	Gets array filled with parameters names from the context.  
Public Method	GetStrings	Gets the array filled with strings from the context. (Additional to the parameters)  
Public Method	SetContextParameter	Sets a block of context parameters (as ContextParameterBlock object).  
Public Method	SetEContext	For internal use only.  
Public Method	SetStrings	Sets the array filled with strings from the context. (Additional to the parameters)  
### ContextParameterBlock Class
A Parameter block for a context. This parameterblock can have System::Object^ as parameters. This block can be used to add objects to a context and work with this objects p.e. inside an action.
Eplan.EplApi.Base.ContextParameterBlock
```csharp 
public class ContextParameterBlock 
```
Public Constructors
Public Constructor	ContextParameterBlock Constructor	Default constructor.  
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of ContextParameter object.  
Public Method	Get	Get one object with this name  
Public Method	GetList	Get the list saved in this block  
Public Method	Set	Set one object with a name  
Public Method	SetList	Set a list for this block  
### Decider Class
This class implements the standard EPLAN decider dialog.
Inheritance Hierarchy
Eplan.EplApi.Base.Decider
```csharp 
public class Decider 
```
Example of using Decider class:
```csharp 
Decider eDecision = new Decider();
EnumDecisionReturn eAnswer = eDecision.Decide(eOkCancelDecision, "Show some dialog text", "Eplan Decider", eOK, eOK);
if (eAnswer == eOK)
{
    // Do your work
}
```
Public Constructors
Public Constructor	Decider Constructor	Create a new Decider Object.  
Public Methods
Public Method	Decide	Overloaded. decide shows a ListSelect dialog.  
Public Method	Dispose	Destructor for deterministic finalization of Decider object.  
### EplAssert Class
The EplAssert class. When the advaced mode is activated in ELogFileConfigTool, Asserts are written to the epllog.txt Its also possible to activate a debugger break. Set the registry value User / Software / Eplan / Eplan W3 / Assert / BreakOnAssert to true, and the debugger will stop at a failed assert.
Eplan.EplApi.Base.EplAssert
```csharp 
public class EplAssert 
```
Example of EplAssert:
```csharp 
object testObject = null;
Eplan.EplApi.Base.EplAssert oAssert= new Eplan.EplApi.Base.EplAssert();
oAssert.Assert (testObject != null, "The testobject must not be null!");
```
Public Constructors
Public Constructor	EplAssert Constructor	 
Public Methods
Public Method	Assert	A Delevoper Assertion. When the boolean Expression fails, the debugged application fails into the debugger. Some Text is written to the EplLog.txt  
### EplTrace Class
Trace the output to the EplLog.txt file. This Trace class works in debug and release mode, while the trace listener works only in debug mode. Traces are written when the registry key HKCU / Software / Eplan / Eplan W3 / Trace / \-ModuleName- is found.
Eplan.EplApi.Base.EplTrace
```csharp 
public class EplTrace 
```
Example of TRACE outputs
```csharp 
Eplan.EplApi.Base.EplTrace oTrace= new Eplan.EplApi.Base.EplTrace();
oTrace.Trace ("Eplan.EplApi.Base", "Start executing function abc");
```
Public Constructors
Public Constructor	EplTrace Constructor	 
Public Methods
Public Method	Trace	Overloaded. Writes the text to EplLog.txt when Trace is on.  
### FileSelectDecisionContext Class
This class can be used for an standard eplan decider
Eplan.EplApi.Base.FileSelectDecisionContext
```csharp 
public class FileSelectDecisionContext 
```
Example of using Decider class with a FileSelectDecisionContext :
```csharp 
FileSelectDecisionContext fileContext = new FileSelectDecisionContext("ExlSheetSelector", EnumDecisionReturn.eCANCEL);
fileContext.Title = "Select Excel file";
fileContext.AllowMultiSelect = false;
fileContext.DefaultExtension = "xls";
fileContext.AddFilter("Excel 97 files (*.xls)", "*.xls");
fileContext.AddFilter("Excel files (*.xlsx)", "*.xlsx");
fileContext.AddFilter("Fenstermakro, Symbolmakro (*.ema, *.ems)", "*.ema;*.ems");
fileContext.AddFilter("All files (*.*)", "*.*");

Decider oDecision = new Decider();
EnumDecisionReturn eAnswer = oDecision.Decide(fileContext);
if (eAnswer != EnumDecisionReturn.eOK)
{
    return true;
}
string sExlFile = fileContext.GetFiles()[0];
```
Public Constructors
Public Constructor	FileSelectDecisionContext Constructor	Overloaded.   
Public Properties
Public Property	AllowMultiSelect	Set or get the flag for multi selection.  
Public Property	CustomDefaultPath	Set or get the CustomDefaultPath. This is the path the File Select Dialog opens first. The second time the path is used the user has selected the last time. Then the context menu "Set to standard" will select this path again.  
Public Property	DefaultExtension	The default extension of the files to select.  
Public Property	DefaultFilename	The default name of a file.  
Public Property	OpenFileFlag	Set or get the openfileflag. Set this flag when you want to open a file Do not set it when you want to save a file.  
Public Property	Title	The title for the decider.  
Public Methods
Public Method	AddFilter	Add a filter which files are shown. When the user selects one filter in the decider dialog, only files of this type are displayed.  
Public Method	Dispose	Destructor for deterministic finalization of FileSelectDecisionContext object.  
Public Method	GetFiles	Get all the files the user has selected in the decider dialog.  
### ISOCode Class
Class for managing language codes (abbreviations). MultiLangString can handle these languages.
Eplan.EplApi.Base.ISOCode
```csharp 
public class ISOCode 
```
Public Constructors
Public Constructor	ISOCode Constructor	Overloaded.   
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of ISOCode object.  
Public Method	GetAllLanguages	Determines all set languages.  
Public Method	GetAllLongNames	Returns a list of full names of all the languages.  
Public Method	GetLongName	Overloaded. \Returns the full name of the language  
Public Method	GetNumber	Overloaded. Convert language code to language number  
Public Method	GetString	Overloaded. Returns the language code as a string.  
Public Method	IsValid	Determines whether a valid language has been set.  
Public Method	SetNumber	Sets the language.  
Public Method	SetString	Sets the language.  
### LanguageList Class
Class for managing a list of languages.
Eplan.EplApi.Base.LanguageList
```csharp  
[DefaultMember("Item")]
[DebuggerTypeProxy(System.Collections.ArrayList/ArrayListDebugView)]
[DebuggerDisplay("Count = {Count}")]
```
public class LanguageList : System.Collections.ArrayList 
Public Constructors
Public Constructor	LanguageList Constructor	 
Public Properties
Public Property	Capacity	(Inherited from System.Collections.ArrayList)
Public Property	Count	(Inherited from System.Collections.ArrayList)
Public Property	IsFixedSize	(Inherited from System.Collections.ArrayList)
Public Property	IsReadOnly	(Inherited from System.Collections.ArrayList)
Public Property	IsSynchronized	(Inherited from System.Collections.ArrayList)
Public Property	Item	(Inherited from System.Collections.ArrayList)
Public Property	Language	Determines the ISO code of the given index.  
Public Property	SyncRoot	(Inherited from System.Collections.ArrayList)
Public Methods
Public Method	Add	(Inherited from System.Collections.ArrayList)
Public Method	AddRange	(Inherited from System.Collections.ArrayList)
Public Method	BinarySearch	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	Clear	(Inherited from System.Collections.ArrayList)
Public Method	Clone	(Inherited from System.Collections.ArrayList)
Public Method	Contains	(Inherited from System.Collections.ArrayList)
Public Method	CopyTo	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	GetEnumerator	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	GetRange	(Inherited from System.Collections.ArrayList)
Public Method	IndexOf	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	Insert	(Inherited from System.Collections.ArrayList)
Public Method	InsertRange	(Inherited from System.Collections.ArrayList)
Public Method	LastIndexOf	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	Remove	(Inherited from System.Collections.ArrayList)
Public Method	RemoveAt	(Inherited from System.Collections.ArrayList)
Public Method	RemoveRange	(Inherited from System.Collections.ArrayList)
Public Method	Reverse	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	SetRange	(Inherited from System.Collections.ArrayList)
Public Method	Sort	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	ToArray	Overloaded.  (Inherited from System.Collections.ArrayList)
Public Method	TrimToSize	(Inherited from System.Collections.ArrayList)
### Languages Class
Class for language information.
Eplan.EplApi.Base.Languages
```csharp
public class Languages 
```
Public Constructors
Public Constructor	Languages Constructor	Creates a new Language object.  
Public Properties
Public Property	AlternativeLanguage	Gets alternative language.  
Public Property	GuiLanguage	Gets Gui language.  
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of Languages object. 
### ListSelectDecisionContext Class
This class can be used for a standard Eplan decider
Eplan.EplApi.Base.ListSelectDecisionContext
```csharp
public ref class ListSelectDecisionContext 
```
Example of using Decider class with a ListSelectDecisionContext :
```csharp
StringCollection collection = new StringCollection();
collection.Add("Content 1");
collection.Add("Content 2");
collection.Add("Content 3");

ListSelectDecisionContext listSelectDecisionContext = new ListSelectDecisionContext(collection, "Content 2", "Dialog Title");

Decider oDecision = new Decider();
EnumDecisionReturn eAnswer = oDecision.Decide(listSelectDecisionContext);
if (eAnswer != EnumDecisionReturn.eOK)
{
    return false;
}

if (listSelectDecisionContext.AllowMultiSelect)
{
    StringCollection selectedEntries = listSelectDecisionContext.SelectedEntries;
}
else
{
    long index = listSelectDecisionContext.SelectedIndex;
    string strEntry = listSelectDecisionContext.SelectedEntry;
}
```
Public Constructors
Public Constructor	ListSelectDecisionContext Constructor	Overloaded.   
Public Properties
Public Property	AllowMultiSelect	Set or get the flag for multi selection.  
Public Property	Entries	Gets all entries  
Public Property	SelectedEntries	Gets all selected entries (Use this property if multi selection is enabled)  
Public Property	SelectedEntry	Gets the selected entries  
Public Property	SelectedIndex	Gets the selected index from Entries  
Public Property	Title	The title for the decider.  
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of ListSelectDecisionContext object.  
### LockingException Class
Exception class that signals locking errors in DataModel.
Eplan.EplApi.DataModel.LockingExceptionFailedLockAttempt
```csharp
public ref class LockingException : public BaseException 
```
Public Constructors
Public Constructor	LockingException Constructor	Overloaded.   
Public Properties
Public Property	Data	(Inherited from System.Exception)
Public Property	HelpLink	(Inherited from System.Exception)
Public Property	HResult	(Inherited from System.Exception)
Public Property	InnerException	(Inherited from System.Exception)
Public Property	Message	(Inherited from System.Exception)
Public Property	MessageLevel	Returns the level of message as MessageLevel. (Inherited from Eplan.EplApi.Base.BaseException)
Public Property	NumberOfOccurrences	Returns number of repetitions of consecutive messages with the same text (i.e. error description) which are joined into one item in the system's message tree. (Inherited from Eplan.EplApi.Base.BaseException)
Public Property	Source	(Inherited from System.Exception)
Public Property	StackTrace	(Inherited from System.Exception)
Public Property	TargetSite	(Inherited from System.Exception)
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of BaseException object. (Inherited from Eplan.EplApi.Base.BaseException)
Public Method	FixMessage	Method enters a message in the system-wide message tree. (Inherited from Eplan.EplApi.Base.BaseException)
Public Method	GetAllFailed2LockAsString	returns all object ids of the objects which were not locked. In case this exception was produced while accessing unlocked object in write mode, only one object will be returned (the one which was accessed first).  
Public Method	GetBaseException	(Inherited from System.Exception)
Public Method	GetBookmarkID	Sets a label in the system error message management for getting a section of the 'message tree' (Inherited from Eplan.EplApi.Base.BaseException)
Public Method	GetFirstFailed2LockAsString	returns the object id of the first object which was not locked. .  
Public Method	GetMessageIndex	returns the identifying S- number of a system message (Inherited from Eplan.EplApi.Base.BaseException)
Public Method	GetMessageText	Returns the text of the system message without the index (Inherited from Eplan.EplApi.Base.BaseException)
Public Method	GetObjectData	(Inherited from System.Exception)
Public Method	GetType	(Inherited from System.Exception)
Public Method	ToString	(Inherited from System.Exception)
### MultiLangString Class
This class can save strings in various languages at the same time. Each string can be added, queried, and deleted individually.
Eplan.EplApi.Base.MultiLangString
```csharp 
public ref class MultiLangString 
```
Remarks
When adding a new language string, language-independant string is removed. When adding a language-independant string, other languages are removed.
Public Constructors
Public Constructor	MultiLangString Constructor	Default constructor  
Public Properties
Public Property	InternalString	Sets internal string representation with format validation.  
Public Methods
Public Method	AddString	Adds a string in the requested language.  
Public Method	Clear	Removes the contents.  
Public Method	ContainsData	Returns whether strings are saved in the MultiLanguageString.  
Public Method	DeleteAllStringsExceptFor	Removes unused translations.  
Public Method	DeleteString	Deletes the language setting.  
Public Method	Dispose	Destructor for deterministic finalization of MultiLangString object.  
Public Method	GetAsString	Converts an MultiLangString to a string. The languages are appended to one another, all having the same format.  
Public Method	GetLanguageList	Returns the list of the languages currently saved in this MultiLangString.  
Public Method	GetString	Returns the string in the requested language  
Public Method	GetStringToDisplay	Returns the string that is to be displayed in accordance with the passed language. This may be the string saved for this language or, if there is no such string, a language-independent string.  
Public Method	IsEqual	Compares every string in every language. If a string is different in one language, then == returns FALSE. If an language string exists in one of the MultiLangStrings but not in the others, this function returns FALSE even if the language string is empty.  
Public Method	SetAsString	Sets the contents of a MultiLangString with a string passed as argument using language marker if necessary. If argument is in MultiLangString form, it will be parsed and saved under given languages. Otherwise '??_??@' prefix is added which means that the object is visible the same in every language.  
Public Method	ToString	Returns a string that represents the current object.  
Public Method	Translatable	Indicates whether the MultiLanguageString can be translated.  
Public Operators
public Operator Equality 	Equality operator
### ParserParameter Class
Parameter Class for the usage with UnitParser. Configure the unit and the look of the Parser result.
Eplan.EplApi.DataModel.Graphics.ProjectParserParameter
```csharp 
public ref class ParserParameter 
```
Public Constructors
Public Constructor	ParserParameter Constructor	Constructor  
Public Properties
Public Property	GridSize	The grid size in millimeters. p.e. "4#" means 4 times grid size  
Public Property	Group	The UnitGroup Property. When first UnitID is set,the group is automatically defined by the unit. While setting a Group also the Unit can be changed to the first Unit in new Group if: - new Group is different than the Group of assigned Unit - there is no Unit and Group assigned When new assigned Group is the same like Unit Group, nothing will change. The unitparser can never convert units of different groups  
Public Property	HideUnit	Hide the unit of the parsed result.  
Public Property	HideValue	Hide the value of the parsed result, all other texts (units and additional texts) will remain.  
Public Property	OnlyFirstValue	Display only the first Value.  
Public Property	OnlyUnit	Display only the Unit.  
Public Property	Precision	Set the precision of the result (Values used for calculation: 0 up to 8)  
Public Property	SpaceBetweenUnitAndValue	Add a space between Unit and the value  
Public Property	SuppressFloatingZeroes	Suppress the last zeroes of a floating result.  
Public Property	UnitFromParameter	Get if the unit needs extra parameter to get resolved. Use the project dependend parameter class if this is true.  
Public Property	UnitID	The UnitId Property. Set or get the unit of the parameters.  
Public Property	WithoutLimiters	The unit is NOT separated by one of this chars: blank (){}[].,:;!?/\\  
Public Methods
Public Method	CanParse	Parsing can start when the unitid is not empty  
Public Method	Dispose	Destructor for deterministic finalization of ParserParameter object.  
### PathMap Class
This class enables you access to the functions used for processing strings that could contain EPLAN path variables.
Eplan.EplApi.Base.PathMap
```csharp 
public ref class PathMap 
```
Remarks
Here are available EPLAN path variables: $(PROJPROP_<ID>)Project property. In order to identify such a path variable, the ID of the respective property is included in the name.
Path variable 	Meaning
$(BIN) 	A program directory generated on installation contains the program libraries (*.dll) of the individual modules.
$(CFG) 	A configuration directory generated on installation containing the xml files of the individual modules.
$(CFG_COMPANY) 	Configuration directory generated on installation, contains the company settings.
$(CFG_STATION) 	Configuration directory generated on installation, contains the station settings.
$(CFG_USER) 	Configuration directory generated on installation, contains the user settings.
$(DOC) 	Project-specific directory for documents.
$(EPLAN) 	An upper-level main directory generated on installation.
$(EPLAN_DATA) 	A superior directory for master data, generated on installation.
$(EPLAN_EXECUTABLE) 	The directory to Eplan.exe.
$(ENVVAR_<Variable_Name>) 	OS environment variable.
$(EPLAN_VARIANT) 	Name of the started product variant.
$(EPLAN_VERSION) 	Version number of the used Eplan.
$(EPLAN_VERSION_SHORT) 	Main version number of the used Eplan.
$(IMG) 	Project-specific directory for images.
$(LOCALDATE) 	Current local date.
$(LOCALTIME) 	Current local time.
$(MD_DOCUMENTS) 	The directory for documents defined under Options > Settings > User > Management > Directories.
$(MD_DXFDWG) 	The directory for DXF / DWG files defined under Options > Settings > User >Management > Directories.
$(MD_FCTDEFS) 	The directory for function definitions available under Options > Settings >User > Management > Directories.
$(MD_FORMS) 	The directory for forms defined under Options > Settings > User > Management > Directories.
$(MD_FRAMES) 	The directory for plot frames defined under Options > Settings > User >Management > Directories.
$(MD_IMG) 	The directory for images defined under Options > Settings > User > Management > Directories.
$(MD_JOBFILESERVER) 	Directory for the Batch Server files.
$(MD_MACROS) 	The directory for macros and outlines defined under Options > Settings >User > Management > Directories.
$(MD_MECHANICALMODELS) 	The directory for mechanical models defined under Options > Settings >User > Management > Directories.
$(MD_PARTS) 	The directory for parts defined under Options > Settings > User >Management > Directories.
$(MD_PROJECTS) 	The directory for projects defined under Options > Settings > User >Management > Directories.
$(MD_SCHEME) 	The directory for schemes defined under Options > Settings > User >Management > Directories.
$(MD_SCRIPTS) 	The directory for scripts defined under Options > Settings > User >Management > Directories.
$(MD_SYMBOLS) 	The directory for symbols defined under Options > Settings > User >Management > Directories.
$(MD_TEMPLATES) 	The directory for templates defined under Options > Settings > User >Management > Directories.
$(MD_TRANSLATE) 	The directory for translation files defined under Options > Settings >User > Management > Directories.
$(MD_XML) 	The directory for XML files defined under Options > Settings > User > Management > Directories.
$(P) 	Full project directory of the currently selected project.
$(PROJECTNAME) 	Project name of the currently selected project, without directory path and file extension.
$(PROJECTPATH) 	Full project directory of the currently selected project.
$(RIGHTS_DB_PATH) 	Directory of the user rights database.
$(TMP) 	The directory used by the operating system for temporary files.
For more information about path variables, please refer to EPLAN Help under the topic:
Using EPLAN>User Interface>Reference>Dialog Select Path variable.
Public Constructors
Public Constructor	PathMap Constructor	Default constructor  
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of PathMap object.  
Public Methodstatic (Shared in Visual Basic)	ReSubstitutePath	Overloaded. Substitute values with variable strVariableName. Returns the changed path.  
Public Methodstatic (Shared in Visual Basic)	ReSubstitutePathForDisplay	Substitute values with variables. Returns the changed path. Ignores all variables which are not visible in P8 Dialogs.  
Public Methodstatic (Shared in Visual Basic)	SubstitutePath	Substitutes variables with their values. Returns the changed path.  
### Progress Class
This class enables you to access the functions of the progress bar in EPLAN.
Eplan.EplApi.Base.Progress
```csharp
public ref class Progress 
```
Remarks
There are different kinds of progress bars. It can be created by functions and passed to another function as a parameter object (often in a Context). Please call Progress::EndPart(true) at the end to close the dialog. Please don't use steps (SetNeededSteps and Step methods) when a nested EPLAN progress (i.e. from API method) could be called afterwards.
Example of using Progress class
```csharp 
Progress oProgress = new Progress("SimpleProgress");
oProgress.ShowImmediately();

//part 1
oProgress.BeginPart(25.0, "");
oProgress.SetActionText("part1");
oProgress.SetNeededSteps(1);
oProgress.Step(1);
System.Threading.Thread.Sleep(2500);    // TODO: Some processing
oProgress.EndPart(false);

//part 2
oProgress.BeginPart(30.0, "");
oProgress.SetNeededSteps(3);            // call SetNeededSteps with the count of steps following
oProgress.SetActionText("part2 step1");
oProgress.Step(1);
System.Threading.Thread.Sleep(1000);    // TODO: Some processing

oProgress.SetActionText("part2 step2");
oProgress.Step(1);
System.Threading.Thread.Sleep(1000);    // TODO: Some processing

oProgress.SetActionText("part2 step3");
oProgress.Step(1);
System.Threading.Thread.Sleep(1000);    // TODO: Some processing
oProgress.EndPart(false);

//part 3
oProgress.BeginPart(45.0, "");          // Here is a sum of 100% reached!
oProgress.SetActionText("part3");
oProgress.SetNeededSteps(1);
oProgress.Step(1);
System.Threading.Thread.Sleep(4500);    // TODO: Some processing
oProgress.EndPart(true);                // The window is destroyed with the call EndPart(true) and the progress is prepared to be destroyed.
```
```csharp 
Progress progress = new Progress("SimpleProgress");
progress.SetAllowCancel(true);
progress.SetAskOnCancel(true);
progress.SetTitle("Replace parts");
progress.ShowImmediately();

DMObjectsFinder finder = new DMObjectsFinder(oProject);
ArticleReference[] articleReferences = finder.GetArticleReferences(null);
int nIteration = 0;
foreach (ArticleReference articleReference in articleReferences)
{
    // Set new values
    progress.BeginPart(100.0 / articleReferences.Length, "Iteration : " + (nIteration++).ToString());
    articleReference.PartNr = "New part number";
    articleReference.VariantNr = "New variant";
    articleReference.StoreToObject();
    new DeviceService().UpdateDevice(articleReference.ParentObject);
    progress.EndPart();
}

progress.EndPart(true);
```
Public Constructors
Public Constructor	Progress Constructor	Overloaded.   
Public Methods
Public Method	BeginPart	Starts a new segment. All parallel segments should result in a sum of 100%.  
Public Method	Canceled	Queries whether the operation was canceled.  
Public Method	Dispose	Destructor for deterministic finalization of Progress object.  
Public Method	EndPart	Overloaded. Ends segment and closes the window when it is not used. Don't forget to call it at the end, otherwise a progress dialog may lock P8.  
Public Method	GetProgress	For internal use only.  
Public Method	SetActionText	Sets a new action text.  
Public Method	SetAllowCancel	Allows canceling.  
Public Method	SetAskOnCancel	Asks to confirm the cancel request.  
Public Method	SetNeededParts	Specifies how many segments are required.  
Public Method	SetNeededSteps	Indicates how many steps are required to reach 100%. E.g. used for loops.  
Public Method	SetOverallActionText	Sets a new action text.  
Public Method	SetTitle	Sets the title of the progress bar.  
Public Method	ShowImmediately	Shows the progress bar without any further delay. When ShowImmediately isnt't called the dialog appears later (with delay), it prevents the dialog to show unnecessarily (to prevent that the progress flickers up for a short running actions).  
Public Method	ShowLevel	Specifies the nesting level up to which a display is made.  
Public Method	Step	Uses a step  
### ProgressFactory Class
This class can be used for OfflineApplications. With RegisterProgress a progress can be installed in Eplan. UnregisterProgress removes this progress from Eplan again.
Eplan.EplApi.Base.ProgressFactory
```csharp 
public ref class ProgressFactory 
```
Public Constructors
Public Constructor	ProgressFactory Constructor	 
Public Methods
Public Methodstatic (Shared in Visual Basic)	RegisterProgress	Registers the progress in the eplan framework  
Public Methodstatic (Shared in Visual Basic)	UnRegisterProgress	unRegisters the progress from the eplan framework  
### Range Class
Range of setting values
Eplan.EplApi.Base.Range
```csharp 
public ref class Range 
```
Public Constructors
Public Constructor	Range Constructor	 
Public Fields
Public Field	FromValue	Minimal value(begin, start)  
Public Field	ToValue	Maximal value(end, stop)  
### SchemeSetting Class
Class for editing settings that are grouped into schemes
Eplan.EplApi.DataModel.ProjectSchemeSetting
```csharp 
public ref class SchemeSetting 
```
Example of using SchemeSetting class
```csharp
SchemeSetting oSchemeSetting = new SchemeSetting();
oSchemeSetting.Init("USER.DXF.SCHEMES");
string strSchemeName = "DXFSchemeToSelect";
if (oSchemeSetting.CheckIfSchemeExists(strSchemeName))
{
    oSchemeSetting.SetScheme(strSchemeName);
    int iExportFormatVersion = oSchemeSetting.GetNumericSetting("EXPORT.FORMAT_VERSION", 0);
}
```
Public Constructors
Public Constructor	SchemeSetting Constructor	Overloaded.   
Public Properties
Public Property	Description	Returns a multilingual description text of the scheme.  
Public Property	MLangName	Returns a multilingual scheme name.  
Public Property	ReadOnly	Gives write permission to settings of this scheme.  
Public Methods
Public Method	CheckIfSchemeExists	Checks whether a scheme is defined.  
Public Method	CopyScheme	Copy an existing scheme.  
Public Method	CountSetting	Number of additional settings existing under the specified setting name.  
Public Method	CreateScheme	Create a new scheme with a specified name, description and the node name for the settings. The data for the new scheme is specified by P8 for each scheme type. The data is the same as the new button in the scheme dialog of P8.  
Public Method	Dispose	For internal use only. Needed if the scheme exists in a project's settings Destructor for deterministic finalization of SchemeSetting object.  
Public Method	ExportScheme	Export a scheme to file.  
Public Method	ExportSchemes	Export all schemes to file.  
Public Method	GetBoolSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetCount	Returns the number of various schemes in this scheme.  
Public Method	GetDoubleSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetLastUsed	Returns the last used scheme name (node LastUsed).  
Public Method	GetLocalizedNameSettingPath	Returns Setting path to the localized name of this scheme.  
Public Method	GetMultiLangStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetName	Returns a language-independent, internal scheme identifier.  
Public Method	GetNodeHandle	Returns the SettingNode of the data node of the current setting. The individual settings can now be accessed via the functions of the SettingNode.  
Public Method	GetNumericSetting	Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.  
Public Method	GetStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	ImportScheme	Import a scheme from file.  
Public Method	ImportSchemes	Import all schemes from file.  
Public Method	Init	Initializes object with a settings node path.  
Public Method	RemoveScheme	Remove a new scheme.  
Public Method	ResetScheme	Sets LastUsed as the current scheme.  
Public Method	Set	Setup internal members  
Public Method	SetBoolSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetDoubleSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetLastUsed	Sets the strName scheme as the current one. Value in node LastUsed will be strName  
Public Method	SetMultiLangStringSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetNumericSetting	Sets the value of settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type.  
Public Method	SetScheme	Overloaded. Sets a scheme by its name (LastUsed remains unchanged!)  
Public Method	SetStringSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
### SettingNode Class
Allows access to settings and relative access to setting-nodes. A setting key consists of a number of sections separated by '.' Each section except the last one is called a setting-node. Setting-nodes and settings together build the settings tree. The settings are the leaves of this tree. The SettingNode class helps iterating trough the nodes and e.g. gives you the possibility to delete a node completely.
Eplan.EplApi.DataModel.ProjectSettingNode
```csharp
public class SettingNode 
```
Remarks
Due to changes in EPLAN, it may happen that settings will change their type or name or that some settings will be completely removed. We cannot guarantee the long-term compatibility of settings. When updating to a newer version, please check your source code, whether the settings you use are still working.
Example of using relative path to access entries
```csharp 
// Create setting node with path STATION.AF.Service.Actions.ActionNewModell
SettingNode oSettingNode = new SettingNode("STATION.AF.Services.Actions.ActionNewModell");
// Set or get setting relative to the path of the node
oSettingNode.SetStringSetting("ModuleName.10", "Service3DLog", 0);
string str = oSettingNode.GetStringSetting("ModuleName.10", 0);
```
Example of merging 2 nodes
```csharp 
SettingNode oTestNode1 = new SettingNode("STATION.AF.Services.Actions.ActionNewModell");
Console.WriteLine(oTestNode1.GetCountOfNodes().ToString()); //  1

SettingNode oTestNode2 = new SettingNode("STATION.AF.Services.Actions.AdjustFromAllLineToSingleLineAndOverview");
Console.WriteLine(oTestNode2.GetCountOfNodes().ToString()); //  1

oTestNode1.MergeWithNode(oTestNode2);
Console.WriteLine(oTestNode1.GetCountOfNodes().ToString()); //  2
```
Example of listing sub-nodes
```csharp 
SettingNode oSettingNode = new SettingNode("STATION.AF.Modules");
StringCollection oSubnodes = new StringCollection();
oSettingNode.GetListOfNodes(ref oSubnodes, false);
foreach (string sSubNode in oSubnodes)
{
    SettingNode oSubNode = oSettingNode.GetSubNode(sSubNode);
    Console.WriteLine(oSubNode.GetNodePath());
}
```
Public Constructors
Public Constructor	SettingNode Constructor	Overloaded.   
Public Methods
Public Method	AddBoolDefault	Defines a new setting for a boolean default.  
Public Method	AddBoolSetting	Defines a new setting for a boolean value.  
Public Method	AddDoubleDefault	Defines a new setting for a double default.  
Public Method	AddDoubleSetting	Defines a new setting for a double value.  
Public Method	AddMultiLangStringDefault	Defines a new setting for a multilanguage string default.  
Public Method	AddMultiLangStringSetting	Defines a new setting for a multilanguage string value.  
Public Method	AddNumericDefault	Defines a new setting for a numeric default.  
Public Method	AddNumericSetting	Defines a new setting for a numeric value.  
Public Method	AddStringDefault	Defines a new setting for a string default.  
Public Method	AddStringSetting	Defines a new setting for a string value.  
Public Method	ClearSetting	Overloaded. Deletes the value. The setting definition is maintained.  
Public Method	DeleteSetting	Resets an individual setting to the value of the corresponding default setting. If it has no default setting, the setting is deleted.  
Public Method	Dispose	Destructor for deterministic finalization of SettingNode object.  
Public Method	ExistSetting	Verifies whether specified setting exists.  
Public Method	ForceReload	Reloads settings node.  
Public Method	GetBoolSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetCountOfNodes	Determines the number of child nodes.  
Public Method	GetCountOfSettings	Determines the number of child settings (subordinate settings).  
Public Method	GetDoubleSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetListOfAllSettings	Determines all settings.  
Public Method	GetListOfNodes	Determines all settings nodes.  
Public Method	GetListOfSettings	Determines all settings of this node.  
Public Method	GetMultiLangStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetNodePath	Determines the path of this node.  
Public Method	GetNodePathDot	Determines the path of this node.  
Public Method	GetNumericSetting	Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.  
Public Method	GetParentNode	Determines the parent node.  
Public Method	GetStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetSubNode	Determines a child node.  
Public Method	MergeWithNode	Merges settings nodes.  
Public Method	ResetNode	Resets the node to default. All settings inside are deleted and copied from defaults again.  
Public Method	Set	Defines the path to the settings node.  
Public Method	SetBoolSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetDoubleSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetMultiLangStringSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	SetNumericSetting	Sets the value of project settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type.  
Public Method	SetStringSetting	Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.  
Public Method	Write	Writes all settings to a file.  
### Settings Class
Settings are used to save values of variables beyond the runtime of the program and to make them available again the next time program is run (similar to the Windows registry). A setting has a unique identifier in the system. A value or a list of values can be saved to a setting. It is possible to group settings into structures SchemeSetting.
Eplan.EplApi.Base.Settings
```csharp 
public ref class Settings : public ISettings  
```
Remarks
Due to changes in EPLAN, it may happen that settings will change their type or name or that some settings will be completely removed. We cannot guarantee the long-term compatibility of settings. When updating to a newer version, please check your source code, whether the settings you use are still working.
Access to a setting of the system
```csharp 
try
{
  String strGuiLanguage= new Settings().GetStringSetting("USER.SYSTEM.GUI.LANGUAGE", 0);
  new Decider().Decide(EnumDecisionType.eOkDecision, "The user interface language is set to: "+ strGuiLanguage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
}
catch (BaseException exc)
{
  String strMessage= exc.Message;
  new Decider().Decide(EnumDecisionType.eOkDecision, "Exception: " + strMessage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
}
```
Public Constructors
Public Constructor	Settings Constructor	Default constructor  
Public Methods
Public Method	AddBoolDefault	Defines a new setting for a boolean default.  
Public Method	AddBoolSetting	Defines a new setting for a boolean value.  
Public Method	AddDoubleDefault	Defines a new setting for a double default.  
Public Method	AddDoubleSetting	Defines a new setting for a double value.  
Public Method	AddMultiLangStringDefault	Defines a new default setting for a multilanguage string value.  
Public Method	AddMultiLangStringSetting	Defines a new setting for a multilanguage string value.  
Public Method	AddNumericDefault	Defines a new setting for a numeric default.  
Public Method	AddNumericSetting	Defines a new setting for a numeric value.  
Public Method	AddStringDefault	Defines a new setting for a string default.  
Public Method	AddStringSetting	Defines a new setting for a string value.  
Public Method	DeleteSetting	Resets an individual setting to the value of the corresponding default setting. If it has no default setting, the setting is deleted.  
Public Method	Dispose	Destructor for deterministic finalization of Settings object.  
Public Method	ExistSetting	Verifies whether specified setting exists.  
Public Method	GetBoolDefault	Returns default boolean value of a setting. The index starts at 0.  
Public Method	GetBoolSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetCountOfDefaultValues	Returnes the number of default values of a setting.  
Public Method	GetCountOfValues	Returnes the number of values of a setting.  
Public Method	GetDescription	\Returns the description of a setting.  
Public Method	GetDoubleDefault	Returns default double value of a setting. The index starts at 0.  
Public Method	GetDoubleSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetExpandedStringSetting	Returns the value of a string setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. If this path is identified via an EPLAN path (e.g. $Eplan, $MD, ...) this identifier is resolved.  
Public Method	GetMultiLangStringDefault	Returns default MultiLangString value of a setting. The index starts at 0.  
Public Method	GetMultiLangStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetNumericDefault	Returns default numeric value of a setting. The index starts at 0.  
Public Method	GetNumericSetting	Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.  
Public Method	GetStringDefault	Returns default string value of a setting. The index starts at 0.  
Public Method	GetStringSetting	Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.  
Public Method	GetTypeOfSetting	Returns the type of the setting.  
Public Method	IsMainNodeReadOnly	Verifies whether the main node (COMPANY / STATION / USER) of the specified setting is Readonly.  
Public Method	ReadSettings	Imports a settings xml file and sets all the settings it contains.  
Public Method	RemoveAllIndexedSetting	Removes all indexed setting.  
Public Method	SetBoolSetting	Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.  
Public Method	SetDoubleSetting	Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.  
Public Method	SetMultiLangStringSetting	Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.  
Public Method	SetNumericSetting	Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.  
Public Method	SetStringSetting	Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.  
Public Method	WriteSetting	Exports the specified setting to an XML file.  
### SysMessagesCollection Class
Class that represents the system-wide message tree. The collection contains the system messages as BaseException objects.
Eplan.EplApi.Base.SysMessagesCollection
```csharp 
public class SysMessagesCollection 
```
Remarks
It is called a message tree, because each message (BaseException) may contain a further inner exception. Only messages of type "Message", "Warning", "Error", and "Fatal Error" are listed. "Assert" and "Trace" are not added to the SysMessagesCollection. Normally Consecutive messages with the same text (i.e. error description) are joined into one item in the system's message tree. Therefore the count of messages in the collection may be different then the count of generated messages. The contents of the collection does not depend on the logging mode, which you can configure either by the "Diagnose dialog" in EPLAN or by the ELogFileConfigToolu.exe in the bin folder of the respective product variant. The logging mode only influences the EplLog.txt file. In advanced logging mode the EplLog.txt file also contains Asserts and Traces. If the logging is set to immediate mode, identical consecutive messages are not joined.
Example of looping over the SysMessagesCollection For further examples, see also in SysMessagesEnumerator class.
```csharp
// check, whether errors occurred
int nBookmark = new Eplan.EplApi.Base.BaseException().GetBookmarkID();
Eplan.EplApi.Base.SysMessagesCollection colSysMsg = new Eplan.EplApi.Base.SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);
foreach(Eplan.EplApi.Base.BaseException osysMsg in colSysMsg)
{

	if (osysMsg != null)
	{
		Console.WriteLine("Fehler: " + osysMsg.ToString());
	}
}
```
Public Constructors
Public Constructor	SysMessagesCollection Constructor	Overloaded.   
Public Properties
Public Property	BookmarkIDEnd	 
Public Property	BookmarkIDStart	 
Public Property	Count	Gets the number of elements contained in the SysMessagesCollection.  
Public Methods
Public Method	GetEnumerator	Returns an enumerator that can iterate through a collection.  
Public Method	GetSysMsgEnumerator	Returns a typed enumerator that can iterate through a collection.  
### SysMessagesEnumerator Class
supports a simple iteration over SysMessagesCollection
Eplan.EplApi.Base.SysMessagesEnumerator
```csharp 
public class SysMessagesEnumerator 
```
Example
iterate over the complete system message tree get all errors and fatal errors of the system message tree since nBookmark was set; how to get a bookmark see BaseException.GetBookmarkID
```csharp 
SysMessagesCollection colSysMsg = new SysMessagesCollection();
SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 
{
BaseException osysMsg = itSysMsg.Current as BaseException;
if (osysMsg != null)
{
	nNr++;
}					

} while(itSysMsg.MoveNext());
```
```csharp
SysMessagesCollection colSysMsg = new SysMessagesCollection(nBookmark, Eplan.EplApi.Base.MessageLevel.Error);
SysMessagesEnumerator itSysMsg = colSysMsg.GetSysMsgEnumerator();
int nNr=0;

itSysMsg.MoveNext(); // move to first item in collection

do 
{
BaseException osysMsg = itSysMsg.Current as BaseException;
if (osysMsg != null)
{
	nNr++;
}					

} while(itSysMsg.MoveNext());
```
Public Constructors
Public Constructor	SysMessagesEnumerator Constructor	Overloaded.   
Public Properties
Public Property	Current	gets the current element in SysMessagesCollection  
Public Methods
Public Method	Dispose	 
Public Method	GetCount	 
Public Method	MoveNext	Advances the enumerator to the next element of SysMessagesCollection  
Public Method	Reset	Sets the enumerator to its initial position, which is before the first element in SysMessagesCollection  
### TraceListener Class
Output of trace messages to the EPLAN system message management (incl. EPLAN log file)
Eplan.EplApi.Base.TraceListener
```csharp
public ref class TraceListener : public System.Diagnostics.TraceListener 
```
Example of TRACE outputs
```csharp 
Eplan.EplApi.Base.TraceListener oTrace= new Eplan.EplApi.Base.TraceListener();
System.Diagnostics.Trace.Listeners.Add(oTrace); // When new trace listeners are created and added, they must be removed again later!

oTrace.WriteLine("Begin Execute"); // Only write to the EPLAN system message management.
System.Diagnostics.Trace.WriteLine("Begin Execute"); // Send to all trace listeners.


oTrace.Close();
System.Diagnostics.Trace.Listeners.Remove(oTrace);
```
Public Constructors
Public Constructor	TraceListener Constructor	 
Public Properties
Public Property	Attributes	(Inherited from System.Diagnostics.TraceListener)
Public Property	Filter	(Inherited from System.Diagnostics.TraceListener)
Public Property	IndentLevel	(Inherited from System.Diagnostics.TraceListener)
Public Property	IndentSize	(Inherited from System.Diagnostics.TraceListener)
Public Property	IsThreadSafe	(Inherited from System.Diagnostics.TraceListener)
Public Property	Name	(Inherited from System.Diagnostics.TraceListener)
Public Property	TraceOutputOptions	(Inherited from System.Diagnostics.TraceListener)
Public Methods
Public Method	Close	(Inherited from System.Diagnostics.TraceListener)
Public Method	CreateObjRef	(Inherited from System.MarshalByRefObject)
Public Method	Dispose()	Destructor for deterministic finalization of TraceListener object. (Inherited from System.Diagnostics.TraceListener)
Public Method	Fail	Overloaded.  (Inherited from System.Diagnostics.TraceListener)
Public Method	Flush	(Inherited from System.Diagnostics.TraceListener)
Public Method	GetLifetimeService	(Inherited from System.MarshalByRefObject)
Public Method	InitializeLifetimeService	(Inherited from System.MarshalByRefObject)
Public Method	TraceData	Overloaded.  (Inherited from System.Diagnostics.TraceListener)
Public Method	TraceEvent	Overloaded.  (Inherited from System.Diagnostics.TraceListener)
Public Method	TraceTransfer	(Inherited from System.Diagnostics.TraceListener)
Public Method	Write	Overloaded. Overridden. Outputs a line to the system message management.  
Public Method	WriteLine	Overloaded. Overridden. Outputs a line to the system message management.  
### UnitParser Class
The UnitParser class. Here it is possible to read the unit from a string and convert it in other units (of the same unit group)
Eplan.EplApi.Base.UnitParser
```csharp 
public ref class UnitParser 
```
Example of using UnitParser class
```csharp 
UnitParser oUnitParser = new UnitParser();

ParserParameter oParserParameter = new ParserParameter();
oParserParameter.UnitID = Unit.Length_cm;

//Set value in cm
oUnitParser.Set("200 cm", oParserParameter);

//Get value in mm
ParserParameter oParserParameter_mm = new ParserParameter();
oParserParameter_mm.UnitID = Unit.Length_mm;

double dValue_mm = oUnitParser.ValueToUnit(oParserParameter_mm);

//Get value in m
ParserParameter oParserParameter_m = new ParserParameter();
oParserParameter_m.UnitID = Unit.Length_m;

double dValue_m = oUnitParser.ValueToUnit(oParserParameter_m);
```
Public Constructors
Public Constructor	UnitParser Constructor	The Constructor  
Public Methods
Public Method	Dispose	Destructor for deterministic finalization of UnitParser object.  
Public Method	GetBaseUnit	Get the base unit of the parsed result of this unit group.  
Public Method	GetBaseValue	Get the value of the parsed result in the base unit of this unit group.  
Public Method	GetUnit	Get the unit of the parsed result.  
Public Method	GetValue	Get the value of the parsed result.  
Public Method	Set	Overloaded. The start of any parse. Set the number and the unit to parse and fill the unit of this text in the parser parameters.  
Public Method	ToDisplay	Convert the value to a new unit (of parameterForConversion) of this group and make a display string out of it.  
Public Method	ValueToUnit	Convert the value to a new unit (of parameterForConversion) of this group.  

