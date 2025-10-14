You can write a script to react on EPLAN events. To do this, you must declare at least one function of the script as an event handler using the  [DeclareEventHandler()]  attribute and load the script.

It is even possible to handle event parameters. However, you need to know the event parameters in advance.

The following two examples show scripts that respond to events when loaded.

The script in the first example reacts to the  onMainStart  event. The function  MyEventHandlerFunction  in the class  SimpleEventHandler  is registered as event handler for the  onMainStart  event. When this event is raised in EPLAN, the function is called.

The second example shows an event handler script that catches any  onActionStart.String  event. There is an event parameter for the name of the action.

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

public class SimpleEventHandler
{
    [DeclareEventHandler("onMainStart")]
     public void MyEventHandlerFunction()
     {
           new Decider().Decide(EnumDecisionType.eOkDecision, "MyEventHandlerFunction was called!","SimpleEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
           return;
     }
} 

public class SimpleEventHandler
{
    [DeclareEventHandler("onActionStart.String.*")]
    public long MyEventHandlerFunction2(IEventParameter iEventParameter)
    {
        try
        {
            EventParameterString oEventParameterString= new EventParameterString(iEventParameter);
            String strActionName= oEventParameterString.String;
            new Decider().Decide(EnumDecisionType.eOkDecision, "Action " + strActionName + " was started!","MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
        }
        catch (System.InvalidCastException exc)
        {
            String strExc= exc.Message;
            new Decider().Decide(EnumDecisionType.eOkDecision, "Parameter error: " + strExc, "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
        }
        return 0;
    }
}
```

```

Public Class SimpleEventHandler

   <DeclareEventHandler("onMainStart")>  _
   Public Sub MyEventHandlerFunction()
      Dim dec As Decider = New Decider
      dec.Decide(EnumDecisionType.eOkDecision, "MyEventHandlerFunction was called!", "SimpleEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
   End Sub 'MyEventHandlerFunction
End Class 'SimpleEventHandler

 

Public Class SimpleEventHandler

   <DeclareEventHandler("onActionStart.String.*")>  _
   Public Function MyEventHandlerFunction2(iEventParameter As IEventParameter) As Long
   Dim dec As Decider = New Decider
      Try
         Dim oEventParameterString As New EventParameterString(iEventParameter)
         Dim strActionName As [String] = oEventParameterString.String
         dec.Decide(EnumDecisionType.eOkDecision, "Action " + strActionName + " was started!", "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

      Catch exc As System.InvalidCastException
         Dim strExc As [String] = exc.Message
         dec.Decide(EnumDecisionType.eOkDecision, "Parameter error: " + strExc, "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
      End Try

      Return 0
   End Function 'MyEventHandlerFunction2
End Class 'SimpleEventHandler
```

