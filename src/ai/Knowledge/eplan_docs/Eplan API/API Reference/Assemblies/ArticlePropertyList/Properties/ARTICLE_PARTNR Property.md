# ARTICLE_PARTNR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PARTNR().html

---

Part number # 22001.

Syntax

**C#**
**C++/CLI**


public PropertyValue ARTICLE_PARTNR {get; set;}

public:

property PropertyValue^ ARTICLE_PARTNR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The part number is identifying for a part, it combines the variants of a part. In the case of part variants, the combination of part number and variant designation is the identifier. During entry as many characters as you wish are possible for the part number, but only the first 96 characters in the UTF-8 format are identifying.
