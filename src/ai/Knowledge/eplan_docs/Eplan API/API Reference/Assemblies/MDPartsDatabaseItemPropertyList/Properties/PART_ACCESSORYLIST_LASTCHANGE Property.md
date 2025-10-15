# PART_ACCESSORYLIST_LASTCHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ACCESSORYLIST_LASTCHANGE().html

---

Last editor / Modification date (accessory list) # 22958.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue PART_ACCESSORYLIST_LASTCHANGE {get; set;}

public:

property MDPropertyValue^ PART_ACCESSORYLIST_LASTCHANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Last change of the accessory list (hierarchy level "Accessory list" in parts management). Shows the sign-in name of the user who last edited the record along with the date and time of the last change. The time is output in the local time of the user in accordance with the set time zone.
