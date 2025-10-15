# FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_STARTYPOS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic670.html

---

Y starting point: Clamping space # 36081.

Syntax

**C#**
**C++/CLI**


public PropertyValue FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_STARTYPOS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_STARTYPOS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

The properties for the clamping space expansion describe the expansion of a clamping space relative to the item edge. Enter the coordinate values of the starting point or the end point of the clamping space, for example "1 mm" for the starting point or "5 mm" for the end point.
