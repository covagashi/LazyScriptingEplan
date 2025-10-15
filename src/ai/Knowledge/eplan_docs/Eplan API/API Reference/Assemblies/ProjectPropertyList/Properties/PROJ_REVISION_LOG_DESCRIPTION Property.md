# PROJ_REVISION_LOG_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_DESCRIPTION(Int32).html

---

Revision comment (change tracking) # 10156.

Syntax

**C#**
**C++/CLI**


public PropertyValue PROJ_REVISION_LOG_DESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_DESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Revision comment (change tracking), max. 1,000 allowed.
