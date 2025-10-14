# ARTICLEREF_AML_GUID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_AML_GUID().html

---

AutomationML GUID (accessories) # 40348.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLEREF_AML_GUID {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLEREF_AML_GUID {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

In this property the GUIDs for accessory parts are stored in AutomationML AR APC format during the PLC data exchange. All parts that are entered at the positions 2 to 50 on the Parts tab in the property dialog of a main function are considered to be accessories. The GUID is generated automatically and should normally not be modified manually.



See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_AML_GUID.html)