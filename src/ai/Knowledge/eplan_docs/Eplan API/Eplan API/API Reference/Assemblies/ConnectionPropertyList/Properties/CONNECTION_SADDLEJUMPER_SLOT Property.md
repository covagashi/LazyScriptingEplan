# CONNECTION_SADDLEJUMPER_SLOT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SADDLEJUMPER_SLOT().html

---

Saddle jumper slot # 31163.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_SADDLEJUMPER_SLOT {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_SADDLEJUMPER_SLOT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

This property can be used to manage up to five saddle jumper slots at saddle jumper connections. The "Automatic" setting is the default setting. In this case only two saddle jumper slots (for the internal and external sides of the terminal connection point) are managed and the saddle jumpers are generated depending on the "internal / external" setting of the respective terminal connection point. Alternatively you can assign a specific saddle jumper slot to the connection by using the setting "Saddle jumper slot 1" to "Saddle jumper slot 5".



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_SADDLEJUMPER_SLOT.html)