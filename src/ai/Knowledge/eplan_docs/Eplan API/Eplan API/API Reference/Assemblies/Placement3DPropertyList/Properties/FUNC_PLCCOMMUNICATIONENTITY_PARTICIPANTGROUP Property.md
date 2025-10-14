# FUNC_PLCCOMMUNICATIONENTITY_PARTICIPANTGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic631.html

---

Node group (Interbus) # 20130.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_PARTICIPANTGROUP( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_PARTICIPANTGROUP {
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

This property is no longer in use and only taken into consideration in old projects. Grouping element in Interbus systems. Using the index, you can differentiate between up to 10 groups.



See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic2058.html)