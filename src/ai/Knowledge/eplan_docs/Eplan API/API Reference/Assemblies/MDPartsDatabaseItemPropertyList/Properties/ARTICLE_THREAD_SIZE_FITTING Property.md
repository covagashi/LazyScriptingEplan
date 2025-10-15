# ARTICLE_THREAD_SIZE_FITTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_THREAD_SIZE_FITTING().html

---

Thread dimension (fitting) # 26109.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_THREAD_SIZE_FITTING {get; set;}

public:

property MDPropertyValue^ ARTICLE_THREAD_SIZE_FITTING {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specific dimensions of the thread that is used in a fitting. This typically includes the diameter and the pitch of the thread. Example: For a water tap, the thread dimension of the fitting is "G1/2". This corresponds to a cylindrical thread with an outside diameter of about 21 mm.
