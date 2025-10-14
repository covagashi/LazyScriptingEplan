# FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED().html

---

Marked for deletion # 20186.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

Marks functions or connections so that these can be found and deleted with a check run.

During the import and synchronization of the PLC data and assignment lists PLC objects (meaning PLC boxes, connection points and addresses) are marked if the respective function is only contained in the Eplan target project, but is not part of the imported PLC data.

During an AutomationML import functions are marked if the respective function is only contained in the Eplan target project, but is not part of the imported AML data.

During an import from Harness proD functions or connections that were deleted in Harness proD are marked in Eplan.



See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED.html)