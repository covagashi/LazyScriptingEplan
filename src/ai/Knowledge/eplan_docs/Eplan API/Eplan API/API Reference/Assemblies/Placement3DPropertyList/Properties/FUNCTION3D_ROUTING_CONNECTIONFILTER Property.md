# FUNCTION3D_ROUTING_CONNECTIONFILTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ROUTING_CONNECTIONFILTER().html

---

Layout space: Connection filter # 36026.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_ROUTING_CONNECTIONFILTER {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_ROUTING_CONNECTIONFILTER {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Filter for generating routing path networks. Is used for routing to control which connections may be routed along which routing tracks (channel, manual routing path, routing range, wiring cut-out). Connection filters are taken into account only if the "Layout space: Routing track specification" (ID 31094) property has not been activated.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ROUTING_CONNECTIONFILTER.html)