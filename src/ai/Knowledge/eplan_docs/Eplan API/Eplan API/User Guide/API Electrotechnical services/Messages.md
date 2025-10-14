# Messages

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Messages.html

---

As an API developer, you can add new electrotechnical messages to Eplan and write them to the message management.

In order to create a new message, add a class to your project that inherits from the Eplan.EplApi.EServices.Message class.

The  Eplan.EplApi.EServices.Message class declares 3 functions:

1. The parameters of the  OnRegister()  function define the properties of the message and how it is registered in Eplan.
2. The  GetMessageText()  function returns the message text that is displayed in dialogs if requested by Eplan.
3. The  DoHelp()  function is called by the system if Eplan requests help on the message.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

public class Message1 : Eplan.EplApi.EServices.Message
{
    public override void OnRegister(ref string creator, ref IMessage.Region eRegionId, ref int iMessageId,
      ref IMessage.Classification eClassification, ref int iOrdinal)
    {
        creator = "Creator name";
        eRegionId = IMessage.Region.Externals;
        iMessageId = 25;
        eClassification = IMessage.Classification.Error;
        iOrdinal = 20;
        return;
    }
    public override System.String GetMessageText()
    {
        // TODO: Provide text from resource in active GUI language
        return "Message text for %1!s! from Eplan.EplAddIn.Demo.Messages";
    }
    public override void DoHelp()
    {
        new Decider().Decide(EnumDecisionType.eOkDecision, "DoHelp was called!", "Eplan.EplAddIn.Demo.Messages", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
        // TODO: activate help for this message
    }
}
```

```

Public Class Message1
   Implements Eplan.EplApi.EServices.Message
   Public Sub OnRegister(ByRef creator As System.String, ByRef eRegionId As IMessage.Region, ByRef iMessageId As Integer, _
                          ByRef eClassification As IMessage.Classification, ByRef iOrdinal As Integer) _
                          Implements Eplan.EplApi.EServices.IMessage.OnRegister
      creator = "Creator name"
      eRegionId = IMessage.Region.Externals
      iMessageId = 25
      eClassification = IMessage.Classification.Error
      iOrdinal = 20
      Return
   End Sub 'OnRegister

   Public Function GetMessageText() As System.String Implements Eplan.EplApi.EServices.IMessage.GetMessageText
      ' TODO: Provide text from resource in active GUI language
      Return "Message text for %1!s! from Eplan.EplAddIn.Demo.Messages"
   End Function 'GetMessageText

   Public Sub DoHelp() Eplan.EplApi.EServices.IMessage.DoHelp
      Dim dec As Decider = New Decider
      dec.Decide(EnumDecisionType.eOkDecision, "DoHelp was called!", "Eplan.EplAddIn.Demo.Messages", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
   End Sub 'DoHelp ' TODO: activate help for this message
End Class 'Message
```

It is also possible to create such classes automatically using the Eplan API Add-in Wizard.

### Adding a new message

A registered message can be now added to the message management of Eplan using the PrjMessagesCollection class.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```

var projectMessageCollection = new PrjMessagesCollection(myProject);

IMessage.Region region = IMessage.Region.Externals;
int messageId = 25;

var storableObject1 = myProjectPage.Functions[0] as StorableObject;
var storableObject2 = myProjectPage.Functions[1] as StorableObject;

//Add new message using AddMessage method
projectMessageCollection.AddMessage(
    region,
    messageId,
    "param text 1",
    storableObject1,
    true,
    storableObject2,
    "additional info 2");

//or using BaseProjectMessage class
var newMessage = new BaseProjectMessage(region, messageId, "param text 2", "BECK.BK3100", "additional info 2");
projectMessageCollection.Add(newMessage);
```

```

Dim projectMessageCollection = New PrjMessagesCollection(myProject)

Dim region As IMessage.Region = IMessage.Region.Externals
Dim messageId As Integer = 25

Dim storableObject1 = TryCast(myProjectPage.Functions(0), StorableObject)
Dim storableObject2 = TryCast(myProjectPage.Functions(1), StorableObject)

projectMessageCollection.AddMessage(region, messageId, "param text 1", storableObject1, True, storableObject2, "additional info 2")

Dim newMessage = New BaseProjectMessage(region, messageId, "param text 2", "BECK.BK3100", "additional info 2")
projectMessageCollection.Add(newMessage)
```

### Overriding the text of an existing message

It is **not** possible to change an existing verification by overriding it via API (by setting the same name and a higher Ordinal number). However, you can override an existing message and change the default message text to your own text. You need to implement a message with the same iMessageId and eRegion, but use a higher  iOrdinal, e.g. 50. Other properties of the message will not be affected.

The following example shows how to override the existing message 007005 "Device without main function.":

| C# | Copy Code |
| --- | --- |
| ```  /// This function returns the message text. /// One verification needs always exactly one message text public string GetMessageText() {    return "This device has absolutely no main function!!!!"; }  /// This is the registration function of the message belonging to the verification. /// Parameters: ///   message region ///   message number ///   classification: error, message or info. ///   overload priority public void OnRegister(ref String strCreator, ref Eplan.EplApi.EServices.IMessage.Region eRegion, ref int iMessageId, ref Eplan.EplApi.EServices.IMessage.Classification eClassification, ref int iOrdinal) {    strCreator = "de.Eplan.Demo";    eRegion = IMessage.Region.Devices;    iMessageId = 5;    eClassification = IMessage.Classification.Error;    iOrdinal = 50; // Higher than 20 } ``` | |

See Also

#### Reference

[Message Class](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message.html)

[IMessage Interface](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)