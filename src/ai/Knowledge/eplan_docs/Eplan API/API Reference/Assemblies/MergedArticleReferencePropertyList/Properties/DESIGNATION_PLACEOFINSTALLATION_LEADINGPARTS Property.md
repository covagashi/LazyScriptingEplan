# DESIGNATION_PLACEOFINSTALLATION_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic364.html

---

Installation site (leading identifiers) # 1422.

Syntax

**C#**
**C++/CLI**


public PropertyValue DESIGNATION_PLACEOFINSTALLATION_LEADINGPARTS( 

   int index

) {get; set;}

public:

property PropertyValue^ DESIGNATION_PLACEOFINSTALLATION_LEADINGPARTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 10.
