# INSTANCE_REVISION_LOG_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionPropertyList~INSTANCE_REVISION_LOG_TIME().html

---

Modification time (change tracking) # 19034.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue INSTANCE_REVISION_LOG_TIME {get; set;}
```
```

```
```
public:

property PropertyValue^ INSTANCE_REVISION_LOG_TIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Time at which an object in a revision was modified. This property is displayed by default in the automatically generated revision marker. The time representation can be configured in the project settings. The time is output in the local time of the user in accordance with the set time zone.
