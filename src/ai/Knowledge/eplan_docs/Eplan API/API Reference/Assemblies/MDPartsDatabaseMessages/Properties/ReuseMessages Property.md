# ReuseMessages Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~ReuseMessages.html

---

Determines whether new message can be duplicated in collection. Default value is `true`.

Syntax

**C#**
**C++/CLI**


public bool ReuseMessages {get; set;}

public:

property bool ReuseMessages {

   bool get();

   void set (    bool value);

}


Remarks

If `true` and message of same id exists in collection then no new message will be added to collection. If `false` new message is always added to collection.
