# FRAME_PATHSIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_PATHSIZE(Int32).html

---

Column width # 12102.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FRAME_PATHSIZE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FRAME_PATHSIZE {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Width of grid columns. A max. of 1,000 is allowed.



See Also

#### Reference

[PlotFramePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList.html)
  
[PlotFramePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_PATHSIZE.html)