# DMPLAOBJECT_SEGMENT_ANALOG_PLCOUTPUT_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic860.html

---

Number of digital PLC inputs # 44079.

Syntax

**C#**
**C++/CLI**


public PropertyValue DMPLAOBJECT_SEGMENT_DIGITAL_PLCINPUT_COUNT {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_SEGMENT_DIGITAL_PLCINPUT_COUNT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the digital PLC inputs for the current planning object. Digital PLC addresses are such addresses that have the data type "BOOL". This is not case-sensitive. Inputs and outputs are recognized by the direction of the PLC address.
