Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public void GetParameter( 
   string strParameterName,
   ref string strParameterValue
)
```
```

```
```
public:
void GetParameter( 
   String^ strParameterName,
   String^% strParameterValue
)
```
```

#### Parameters

*strParameterName*
:   Paramter name (input parameter)

*strParameterValue*
:   Parameter value (output parameter)

Remarks

If the parameter exists, strParameterValue contains its value after executing this method. If the parameter is not found, strParameterValue is set to nullptr.



See Also

#### Reference

[RemotingCallingContext Class](Eplan.EplApi.AFu~Eplan.EplApi.RemoteServer.RemotingCallingContext.html)
  
[RemotingCallingContext Members](Eplan.EplApi.AFu~Eplan.EplApi.RemoteServer.RemotingCallingContext_members.html)