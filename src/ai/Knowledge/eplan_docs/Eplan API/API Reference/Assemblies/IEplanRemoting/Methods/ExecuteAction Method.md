# ExecuteAction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~ExecuteAction.html

---

Execute an action synchronously.

Syntax

**C#**
**C++/CLI**


bool ExecuteAction( 

   string strAction,

   ref CallingContext oContext

)

bool ExecuteAction( 

   String^ strAction,

   CallingContext^% oContext

)


#### Parameters

*strAction*
:   Action name.

*oContext*
:   Calling context.
