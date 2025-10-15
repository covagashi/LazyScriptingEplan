# FUNC_SHOWCROSSREFERENCEBLOCK Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_SHOWCROSSREFERENCEBLOCK().html

---

Cross-reference display: Display # 20049.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_SHOWCROSSREFERENCEBLOCK {get; set;}

public:

property PropertyValue^ FUNC_SHOWCROSSREFERENCEBLOCK {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the representation of the cross-reference display:

0 = From project settings

1 = Show by columns

2 = Show by rows.
