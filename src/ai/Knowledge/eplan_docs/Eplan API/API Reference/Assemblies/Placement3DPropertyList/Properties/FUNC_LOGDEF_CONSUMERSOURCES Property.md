# FUNC_LOGDEF_CONSUMERSOURCES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_LOGDEF_CONSUMERSOURCES(Int32).html

---

Connection point logic: Consumer / source to # 20327.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_LOGDEF_CONSUMERSOURCES( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_CONSUMERSOURCES {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Specifies via the connection point number the other connection point to which a consumer or generator (source) is internally connected. Using the index, you can differentiate between up to 100 settings.
