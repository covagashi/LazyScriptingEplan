An add-in can add one or more ribbon commands to the Extensions > API command gropup. Therefore the class  Eplan.EplApi.Gui.RibbonBar  provides a function  AddCommand  which should be called in the  OnRegister()  method of the add-in class:

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

/// <summary>
/// The function is called once during registration add-in.
/// </summary>
/// <param name="bLoadOnStart"> true: In the next Eplan session, add-in will be loaded during initialization</param>
/// <returns></returns>
public bool OnRegister(ref System.Boolean bLoadOnStart)
{
   var ribbonBar= new Eplan.EplApi.Gui.RibbonBar();
   ribbonBar.AddCommand("CSharpAction", "CSharpAction");
   return true;
}

/// <summary>
/// The function is called during unregistration the add-in.
/// </summary>
/// <returns></returns>
public bool OnUnregister()
{
    var ribbonBar = new Eplan.EplApi.Gui.RibbonBar();
    return ribbonBar.RemoveCommand("CSharpAction");
}
```

```

''' <summary>
''' This function is called once the Add-ins through the Framework in the registering.  
''' </summary>
''' <param name="bLoadOnStart"> True:  The Add-in is loaded in the future in system start and the function <seealso cref="OnInit"/> is called. </param>
''' <returns></returns>
Public Function OnRegister(ByRef bLoadOnStart As System.Boolean) As Boolean Implements IEplAddIn.OnRegister
   Dim ribbonBar As Eplan.EplApi.Gui.RibbonBar= New Eplan.EplApi.Gui.RibbonBar
   ribbonBar.AddCommand("CSharpAction", "CSharpAction")
   Return True
End Function 'OnInitGui

''' <summary>
''' This function will remove from called once the Add-ins through the Framework in that the system.
''' </summary>
''' <returns></returns>
Public Function OnUnregister() As Boolean Implements IEplAddIn.OnUnregister
    Dim ribbonBar As New RibbonBar()
    Return ribbonBar.RemoveCommand("CSharpAction")
End Function
```

The function  AddCommand(text, command line)  adds a button (i.e ribbon command) with the text "CSharpAction" and assigns the action "CSharpAction" to it. The button is then visible in Extensions > API command group. It is also possible to add it to a custom command group that exists in either persistent or a custom tab.

Ribbon commands are always assigned to an action. This can be either a custom action (created using the API) or an already existing action.

See Also

#### Scripts

[Adding ribbon items by a script](script_ribbon.html)

#### API Miscellaneous

[Ribbon bar](TheRibbon.html)