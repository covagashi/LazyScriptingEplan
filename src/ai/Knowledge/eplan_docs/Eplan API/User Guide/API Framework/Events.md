# Events

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Events.html

---

EPLAN has its own mechanism to send notifications and to react on notifications. Notifications, also called "**events**", are identified in EPLAN by their names (string). This means there is no specific type of class you send as a notification.

EPLAN and each module in EPLAN can send and handle events without any need to register the event in the system. The EPLAN event mechanism is very flexible. The API user can even send and handle events with new names.

For a list of EPLAN events, please refer to this link: [Eplan.EplApi.ApplicationFramework.Events](API Events.html).

### How to react on EPLAN events?

 To react on an event, just implement an event handler function and register it with the EPLAN  EventHandler  object.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

class MyEventListener
{
    // create an EventHandler object
    Eplan.EplApi.ApplicationFramework.EventHandler myHandler = new
    Eplan.EplApi.ApplicationFramework.EventHandler();
    public MyEventListener()
    {
        // react on the EPLAN event "onActionStart.String.*"
        myHandler.SetEvent("onActionStart.String.*");
        // If the event "onActionStart.String.*" is raised,
        // the function myHandler_EplanEvent should be called
        myHandler.EplanEvent +=  myHandler_EplanEvent;
    }

    private void myHandler_EplanEvent(IEventParameter iEventParameter)
    {
        // TODO: do something, when the event is caught
    }
}
```

```

Class MyEventListener
      ' create an EventHandler object
      Dim myHandler As New Eplan.EplApi.ApplicationFramework.EventHandler()
   Public Sub New()
      ' react on the EPLAN event "onActionStart.String.*"
      myHandler.SetEvent("onActionStart.String.*")
      ' If the event "onActionStart.String.*" is raised,
      ' the function myHandler_EplanEvent should be called
      Dim oEvent As EventHandlerFunction = New EventHandlerFunction(AddressOf myHandler_EplanEvent)
      myHandler.EplanEvent = System.Delegate.Combine(myHandler.EplanEvent, oEvent)
   End Sub 'New
   Private Sub myHandler_EplanEvent(iEventParameter As IEventParameter)
      ' TODO: do something, when the event is caught
   End Sub 'myHandler_EplanEvent
End Class 'MyEventListener
```

Now, you need to create an instance of your event listener class. During the lifetime of this object the event is handled. For example, you can instantiate the object in the API module class of your add-in:

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

public class AddInModule: IEplAddIn
{
    private MyEventListener m_EventHandler;
    ///<summary>
    /// This function is called, when starting EPLAN,
    /// if the add-in is loaded on system startup.
    ///</summary>
    /// <returns></returns>
    ///<seealso cref="OnRegister"/>
     public bool OnInit()
    {
        m_EventHandler = new MyEventListener ();
        return true;
    }
//...
}
```

```

Public Class AddInModule
   Implements IEplAddIn
   Private m_EventHandler As MyEventListener

   '''<summary>
   ''' This function is called, when starting EPLAN,
   ''' if the add-in is loaded on system startup.
   '''</summary>
   ''' <returns></returns>
   '''<seealso cref="OnRegister"/>
   Public Function OnInit() As Boolean Implements IEplAddIn.OnInit
      m_EventHandler = New MyEventListener()
      Return True
   End Function 'OnInit
'...
End Class 'AddInModule
```

### Event parameter

Every event may additionally have parameters of a certain type. For this purpose we have the  EventParameter  classes, like for example  EventParameterString.

The  OnEvent()  function has a generic interface as parameter. It takes the specific  EventParameter  classes as constructor argument. Subsequently it tries to create this parameter object. If the interface does not contain a suitable object, EPLAN throws an exception.

So, when you handle a specific event, you need to know the type of the event parameter beforehand in order to create the correct parameter from the interface.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

private void myHandler_EplanEvent(IEventParameter iEventParameter)
{
    try
    { 
        EventParameterString oEventParameterString = new
        EventParameterString(iEventParameter);
        String strActionName = oEventParameterString.String;
    }
    catch (System.InvalidCastException exc)
    {
        String strexc = exc.Message;
    }
}
```

```

Private Sub myHandler_EplanEvent(iEventParameter As IEventParameter)
    Try
        Dim oEventParameterString As New EventParameterString(iEventParameter)
        Dim strActionName As String = oEventParameterString.String 
    Catch exc As System.InvalidCastException
        Dim strexc As String = exc.Message
    End Try
End Sub 'myHandler_EplanEvent
```

```



```

### Raising events

You can create and send your own events with arbitrary names. However, you have no influence on whether your event is handled somewhere. In the following example an event named "EventFromCSharpAddIn" is raised. The event has a parameter of the type  EventParameterString.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

EventParameterString oEventParamString = new EventParameterString();
oEventParamString.String = "ParameterFromCSharpAddIn";
long lRetVal = new EventManager().Send("EventFromCSharpAddIn", oEventParamString);
```

```

Dim oEventParamString As New EventParameterString()
oEventParamString.String = "ParameterFromCSharpAddIn"
Dim lRetVal As Long = New EventManager().Send("EventFromCSharpAddIn", oEventParamString)
```