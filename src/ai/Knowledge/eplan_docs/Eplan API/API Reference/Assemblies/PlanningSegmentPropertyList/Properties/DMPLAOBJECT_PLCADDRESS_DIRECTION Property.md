# DMPLAOBJECT_PLCADDRESS_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic849.html

---

PLC address: Function text # 44025.

Syntax

**C#**
**C++/CLI**


public PropertyValue DMPLAOBJECT_PLCADDRESS_FUNCTIONTEXT( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PLCADDRESS_FUNCTIONTEXT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

PLC inputs and outputs that are required for controlling can be defined at a planning object. Enter here the function text. The individual PLC inputs and outputs are differentiated via the index, with a maximum of 50.
