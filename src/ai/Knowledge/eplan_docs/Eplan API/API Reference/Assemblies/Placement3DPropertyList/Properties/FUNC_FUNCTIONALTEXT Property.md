# FUNC_FUNCTIONALTEXT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_FUNCTIONALTEXT(Int32).html

---

State # 20285.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_FUNCTIONALTEXT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_FUNCTIONALTEXT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 10.

Indicates the states in the "Functional" representation type. A maximum of 10 states can be defined for the function using the index.
