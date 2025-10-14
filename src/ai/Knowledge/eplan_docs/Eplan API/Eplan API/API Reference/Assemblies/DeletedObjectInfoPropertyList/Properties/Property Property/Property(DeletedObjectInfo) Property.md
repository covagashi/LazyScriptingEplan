# Property(DeletedObjectInfo) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~Property(DeletedObjectInfo).html

---

Method used by operator[] in order to access properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue Property( 
   Properties.DeletedObjectInfo id
) {get; set;}
```
```

```
```
public:
property PropertyValue^ Property {
   PropertyValue^ get(Properties.DeletedObjectInfo id);
   void set (Properties.DeletedObjectInfo id, PropertyValue^ value);
}
```
```

#### Parameters

*id*
:   Identifier of the DeletedObjectInfo's property

#### Property Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [PropertyReadOnlyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyReadOnlyException.html) | PropertyReadOnlyException |
| [SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |



See Also

#### Reference

[DeletedObjectInfoPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList.html)
  
[DeletedObjectInfoPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~Property.html)
  
[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[Properties.DeletedObjectInfo Enumeration](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Properties+DeletedObjectInfo.html)