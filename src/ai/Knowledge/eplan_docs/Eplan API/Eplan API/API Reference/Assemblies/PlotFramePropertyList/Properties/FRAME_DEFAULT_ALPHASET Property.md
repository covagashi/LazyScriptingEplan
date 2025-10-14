# FRAME_DEFAULT_ALPHASET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_DEFAULT_ALPHASET().html

---

String for alphanumeric # 12032.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FRAME_DEFAULT_ALPHASET {get; set;}
```
```

```
```
public:
property PropertyValue^ FRAME_DEFAULT_ALPHASET {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

If an alphanumeric column and row numbering format is specified for a plot frame (ID 12009 or ID 12011), then you enter the value of the column or row designations here. The entry '0123456789ABCDEF', for instance, results in hexadecimal designations.



See Also

#### Reference

[PlotFramePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList.html)
  
[PlotFramePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_DEFAULT_ALPHASET.html)