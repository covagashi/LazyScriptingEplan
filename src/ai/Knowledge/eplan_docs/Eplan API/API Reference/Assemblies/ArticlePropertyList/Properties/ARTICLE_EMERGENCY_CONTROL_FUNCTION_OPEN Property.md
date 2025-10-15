# ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN().html

---

Emergency control function (open) # 26055.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN {get; set;}

public:

property PropertyValue^ ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Safety function in which a device or system is brought into an open position in case of an emergency. Example: A spring return drive that automatically opens the flap in the event of a power failure.
