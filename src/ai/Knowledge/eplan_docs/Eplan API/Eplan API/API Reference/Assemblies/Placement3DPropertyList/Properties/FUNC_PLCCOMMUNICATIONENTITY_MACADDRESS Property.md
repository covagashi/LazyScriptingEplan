# FUNC_PLCCOMMUNICATIONENTITY_MACADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic629.html

---

MAC address # 20128.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_MACADDRESS( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_MACADDRESS {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Media Access Control: Unique identifier of a network device (for example network card or WLAN card). The MAC address is centrally assigned and the first 24 bits identify the respective device manufacturer. Using the index, you can differentiate between up to 10 addresses.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCCOMMUNICATIONENTITY_MACADDRESS.html)