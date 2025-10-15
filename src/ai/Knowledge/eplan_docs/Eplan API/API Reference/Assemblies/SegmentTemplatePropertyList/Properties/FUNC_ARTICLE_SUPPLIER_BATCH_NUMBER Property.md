# FUNC_ARTICLE_SUPPLIER_BATCH_NUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1265.html

---

Supply voltage range # 26624.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNC_ARTICLE_SUPPLY_VOLTAGE_RANGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUPPLY_VOLTAGE_RANGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specified value range of the voltage that can be applied to a device for supplying power.
