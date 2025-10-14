# Property(Cable) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList~Property(Cable).html

---

Method used by operator[] in order to access properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue Property( 
   Properties.Cable id
) {get; set;}
```
```

```
```
public:
property PropertyValue^ Property {
   PropertyValue^ get(Properties.Cable id);
   void set (Properties.Cable id, PropertyValue^ value);
}
```
```

#### Parameters

*id*
:   Identifier of the Cable's property

#### Property Value

[Eplan.EplApi.DataModel.PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [Eplan.EplApi.DataModel.PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [Eplan.EplApi.DataModel.PropertyReadOnlyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyReadOnlyException.html) | PropertyReadOnlyException |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |



See Also

#### Reference

[CablePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList.html)
  
[CablePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList~Property.html)
  
[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[Properties.Cable Enumeration](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Properties+Cable.html)