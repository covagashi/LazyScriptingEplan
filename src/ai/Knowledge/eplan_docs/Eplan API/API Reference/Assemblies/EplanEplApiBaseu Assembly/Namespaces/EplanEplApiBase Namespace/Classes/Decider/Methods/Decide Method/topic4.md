Decide shows the dialog. When the application id in quiet mode, the batch decision is returned. The icon used is an EXCLAMATION.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public EnumDecisionReturn Decide( 
   EnumDecisionType type,
   string strText,
   string strTitle,
   EnumDecisionReturn eDefaultDecision,
   EnumDecisionReturn eBatchDecision
)
```
```

```
```
public:
EnumDecisionReturn Decide( 
   EnumDecisionType type,
   String^ strText,
   String^ strTitle,
   EnumDecisionReturn eDefaultDecision,
   EnumDecisionReturn eBatchDecision
)
```
```

#### Parameters

*type*
:   The type of the decider

*strText*
:   The text to show in the window.

*strTitle*
:   The title of the window

*eDefaultDecision*
:   A default decision, this one is preselected in the dialog.

*eBatchDecision*
:   The decision taken when no dialogs are allowed. used in quiet mode.

#### Return Value

The return value includes the pressed button or error.



See Also

#### Reference

[Decider Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html)
  
[Decider Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider_members.html)
  
[Overload List](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Decide.html)