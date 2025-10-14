What is called an "**action**" in Eplan?

An action is a procedure or function that can be dynamically registered in Eplan. The action is identified by its name and its overload priority. An action can have any number of parameters, which are passed to and from the action via a so-called  ActionCallingContext. Each ribbon button in Eplan is associated with an action that is called up when the ribbon button is clicked.

An add-in can add new actions to Eplan. Actions can be called from the command line and they can be assigned to a new ribbon button. A new action can override an existing action with the same name.

An action is implemented by a class that inherits the interface  IEplAction. You need to add an implementation of all the functions of the interface. An add-in can contain an arbitrary number of actions.

* [C#]

```

public class CSharpAction: Eplan.EplApi.ApplicationFramework.IEplAction
{
    ///<summary>
    ///This function is called when executing the action.
    ///</summary>
    ///<returns>true, if the action performed successfully</returns>
    public bool Execute(Eplan.EplApi.ApplicationFramework.ActionCallingContext ctx )
    {
         new Decider().Decide(EnumDecisionType.eOkDecision, "CSharpAction was called!", "Eplan.EplAddIn.Demo1", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
         // TODO: Add your Code here

         return true;
    }
    ///<summary>
    ///This function is called by the application framework, when registering the add-in.
    ///</summary>
    ///<param name="Name">The action is registered in Eplan under this name</param>
    ///<param name="Ordinal">The action is registered with this overload priority</param>
    ///<returns>true, if OnRegister succeeds</returns>
    public bool OnRegister(ref string Name, ref int Ordinal)
    {
         Name  = "CSharpAction";
         Ordinal    = 20;
         return true;
    }
    ///<summary>
    /// Documentation function for the action, which is called by Eplan on demand
    /// returns the descriptive text for the action itself and if the action takes string parameters
    /// (command line), it also provides the name and description of each parameter
    ///</summary>
    ///<param name="actionProperties"> This object needs to be filled with information about the action
    ///</param>
    public void GetActionProperties(ref Eplan.EplApi.ApplicationFramework.ActionProperties actionProperties)
    {
        actionProperties.Description= "Action test with parameters.";
        // description of first parameter
        Eplan.EplApi.ApplicationFramework.ActionParameterProperties firstParam= new ActionParameterProperties();
        firstParam.Set("Param1", "first test parameter");
        actionProperties.AddParameter(firstParam);
        // description of second parameter
        // Eplan.EplApi.ApplicationFramework.ActionParameterProperties secondParam= new ActionParameterProperties();
        // secondParam.Set("Param2", "Second parameter for test");
        // actionProperties.AddParameter(secondParam);
    }
}
```

The parameter of type  ActionCallingContext  can be used to pass parameters to the action. For extracting the parameter values and for setting parameters (as return parameters!), the class  ActionCallingContext  provides a set of functions:

* [C#]

```

public bool Execute(Eplan.EplApi.ApplicationFramework.ActionCallingContext ctx )
{
   String strParamValue=null;
   ctx.GetParameter("Param1", ref strParamValue);
   // use string parameter ...
   // fill parameter "ReturnParam" with value "return value".
   // the caller of this action can extract the parameter by ctx.getParameter("ReturnParam", ...)
   String strReturnValue= "return value";
   ctx.AddParameter("ReturnParam", strReturnValue);
   return true;
}
```

When an action is assigned to a ribbon button, these items are only enabled if the action is registered and enabled. You can enable / disable a registered action via the  IEplActionEnable  interface.

* [C#]

```

public class TestAction : Eplan.EplApi.ApplicationFramework.IEplAction, Eplan.EplApi.ApplicationFramework.IEplActionEnable
    {
        //IEplAction Members
        #region IEplActionEnable Members
        public bool Enabled(string strActionName, Eplan.EplApi.ApplicationFramework.ActionCallingContext actionContext)
        {
            if (strActionName == "TESTACTION")
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        #endregion
    }
```
