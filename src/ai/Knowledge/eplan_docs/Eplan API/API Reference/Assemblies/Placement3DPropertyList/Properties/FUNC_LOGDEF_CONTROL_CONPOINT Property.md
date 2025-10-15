# FUNC_LOGDEF_CONTROL_CONPOINT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_LOGDEF_CONTROL_CONPOINT(Int32).html

---

Connection point logic: Pressure / control port # 20369.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_LOGDEF_CONTROL_CONPOINT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_CONTROL_CONPOINT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
