# MESSAGEMGMT_MESSAGES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~MESSAGEMGMT_MESSAGES().html

---

Check run messages available # 20930.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue MESSAGEMGMT_MESSAGES {get; set;}
```
```

```
```
public:
property PropertyValue^ MESSAGEMGMT_MESSAGES {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows (after a check run) whether messages occurred for a function or a part. These messages can be viewed in the message management or in the "Messages" tab of the parts management. The property can also be used in the block properties. If messages relating to the function exist, the value "X" is output.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~MESSAGEMGMT_MESSAGES.html)