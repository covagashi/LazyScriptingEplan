# ARTICLE_CONNECTIONCROSSSECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CONNECTIONCROSSSECTION().html

---

Connection point cross-section # 22036.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_CONNECTIONCROSSSECTION {get; set;}

public:

property PropertyValue^ ARTICLE_CONNECTIONCROSSSECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Evaluates a value calculated on the "Properties" tab in parts management and outputs it in a report, e.g. a terminal diagram, and displays it at the terminal in the schematic. At a part with the product group "Relays, contactors" this property refers to the contact.
