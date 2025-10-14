# FUNC_ARTICLE_DEVICE_PROFILE_ACCORDING_TO_BACNET_SPECIFICATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic538.html

---

BACnet: Device profile according to BACnet specification # 26369.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_DEVICE_PROFILE_ACCORDING_TO_BACNET_SPECIFICATION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_DEVICE_PROFILE_ACCORDING_TO_BACNET_SPECIFICATION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A BACnet device profile defines the specific requirements that a device must fulfill in order to communicate with other BACnet-compatible devices. In this property (preset) rules and protocols according to BACnet are specified which are used during the setting of a default configuration.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2011.html)