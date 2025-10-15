# ARTICLE_PLCGROUP_DATALENGTH_INPUTS_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1625.html

---

PLC subdevice 1: Data length (inputs) # 22363.

Syntax

**C#**
**C++/CLI**


public MDPropertyValue ARTICLE_PLCGROUP_DATALENGTH_INPUTS_1 {get; set;}

public:

property MDPropertyValue^ ARTICLE_PLCGROUP_DATALENGTH_INPUTS_1 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Required length in address space for the inputs of this PLC subdevice. The specification is in bits. The address range of the PLC subdevice is determined from the data length together with the start address. Note that there are PLC cards, for example technology modules, which are only assigned to a few inputs / outputs, but still require a larger address range than the one currently occupied. Always enter the maximum required length for the address range of the inputs here.
