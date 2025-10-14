A script consists of at least one public class with at least one public function. This one required function needs to be marked with the attribute  [Start].

The following example shows a very simple script.

* [CS] 


```

public class VerySimpleScript
{
     [Start]
     public void MyFunction()
     {
           new Decider().Decide(EnumDecisionType.eOkDecision, "MyFunction was called!", "VerySimpleScript", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
           return;
     }
}
```

In this example the class "VerySimpleScript" with a function "MyFunction" was created. The function was marked with the attribute  [Start].  
When this script is run using the ribbon **File** > **Extras** > **Interfaces** > **Scripts** > **Run**, the function "MyFunction" is executed and a message box appears:

![This message boy appears, when you run the very simple script.]("This message boy appears, when you run the very simple script.")

A script may contain more than one function. There even can be several classes in a script. However, there may only be exactly one function marked with the  [Start]  attribute!