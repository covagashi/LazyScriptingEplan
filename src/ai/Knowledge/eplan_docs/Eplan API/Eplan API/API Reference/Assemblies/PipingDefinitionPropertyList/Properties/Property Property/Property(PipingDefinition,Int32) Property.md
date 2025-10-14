# Property(PipingDefinition,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~Property(PipingDefinition,Int32).html

---

Method used by operator[] in order to access indexed properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue Property( 
   Properties.PipingDefinition id,
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ Property {
   PropertyValue^ get(Properties.PipingDefinition id, int index);
   void set (Properties.PipingDefinition id, int index, PropertyValue^ value);
}
```
```

#### Parameters

*id*
:   Identifier of the PipingDefinition's property

*index*
:   Index of the PipingDefinition's property

#### Property Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [PropertyReadOnlyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyReadOnlyException.html) | PropertyReadOnlyException |
| [SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |



See Also

#### Reference

[PipingDefinitionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList.html)
  
[PipingDefinitionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PipingDefinitionPropertyList~Property.html)
  
[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[Properties.PipingDefinition Enumeration](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Properties+PipingDefinition.html)