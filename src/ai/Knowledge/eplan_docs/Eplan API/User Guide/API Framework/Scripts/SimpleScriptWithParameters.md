The script functionality does also accept parameters. However, this only makes sense if a parameter can be passed to the script when it is started. This can be done by invoking Eplan via the command line:

W3u.exe ExecuteScript /ScriptFile:"C:\Program Files\EPLAN\EPLAN\Basic\Scripts\EPLAN\SimpleScriptWithParameters.cs" /Param1:"Hello" /Param2:"EPLAN" /Param3:"API developer!" 

When starting Eplan via command line, in order to run a script, the first parameter is the name of the action to be executed. The action for executing scripts is called  ExecuteScript. This action takes the  /ScriptFile  parameter which specifies the name of the script file to be run. Any further parameter (<Param1>,  <Param2>,  <Param3>  etc.) is optional and will be passed to the start function (i.e. the function marked with the  [Start]  attribute) of the script. You can name the further parameters as you wish. In the follwing example they are simply called "Param1", "Param2" and "Param3", but you can just as well give the parameters meaningful names like "Textmodule1", "projectName" or whatever makes sense in your use case.

![](sectionminus.png)Example

In the following example, the script (i.e. the script function) requires 3 string parameters "Param1", "Param2" and "Param3":

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

public class SimpleScriptWithParameters
 {
    [Start]
     public bool FunctionWithParameters(String Param1, String Param2, String Param3)
     {
        new Decider().Decide(EnumDecisionType.eOkDecision,  Param1 + Param2 + Param3 , "SimpleScriptWithParams", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
        return true;
    }
 }
```

```

Public Class SimpleScriptWithParameters

   <Start>  _
   Public Function FunctionWithParameters(ByVal Param1 As String, ByVal Param2 As String, _
                                            ByVal Param3 As String) as Boolean
      Dim dec As Decider = New Decider
      dec.Decide(EnumDecisionType.eOkDecision, Param1 + Param2 + Param3, "SimpleScriptWithParams", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
      Return True
   End Sub 'FunctionWithParameters
End Class 'SimpleScriptWithParameters
```

It is important, that the identifiers (in this example "Param1", "Param2", "Param3") are exactly matching in the command line and in the function!

It is possible to use scripts with  ActionCallingContext  as a parameter. To do that, please look at the following example:

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

public class ScriptWithActionCallingContext
{
    [Start]
    public void FunctionWithActionCallingContext(ActionCallingContext oActionCallingContext)
    {
        string strFirstParam = "";
        string strSecondParam = "";
        oActionCallingContext.GetParameter("strFirstParam", ref strFirstParam);
        oActionCallingContext.GetParameter("strSecondParam", ref strSecondParam);
        string strNewParam = "";
        oActionCallingContext.AddParameter("strNewParam", strFirstParam + strSecondParam);
        oActionCallingContext.GetParameter("strNewParam", ref strNewParam);
        if (strNewParam.Equals(strFirstParam + strSecondParam))
        {
            // TODO: Add some functionality here
        }
    }
}
```

```

Public Class ScriptWithActionCallingContext

<Start>  _
    Public Sub FunctionWithActionCallingContext (ByVal oActionCallingContext As ActionCallingContext)
        Dim strFirstParam As [String] = ""
        Dim strSecondParam As [String] = ""
        oActionCallingContext.GetParameter("strFirstParam", strFirstParam)
        oActionCallingContext.GetParameter("strSecondParam", strSecondParam)
        Dim strNewParam As [String] = ""
        oActionCallingContext.AddParameter("strNewParam", strFirstParam + strSecondParam)
        oActionCallingContext.GetParameter("strNewParam", strNewParam)
        If strNewParam = strFirstParam + strSecondParam Then       
            ' TODO: Add some functionality here
        End If
    End Sub 'FunctionWithActionCallingContext
End Class 'ScriptWithActionCallingContext
```

Using this feature, you can extend the scope of the Eplan command line by your own parameters. If you need to call some API functionality via command line, just create a script. The start function of this script may take parameters and can call other functions with these parameters.

See Also

#### Actions

[ExecuteScript](ExecuteScript.html)