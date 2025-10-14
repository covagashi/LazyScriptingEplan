# SortSchemaData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~SortSchemaData.html

---

Property data represents sort scheme settings for report generation.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string SortSchemaData {get; set;}
```
```

```
```
public:
property String^ SortSchemaData {
   String^ get();
   void set (    String^ value);
}
```
```

Remarks

String contains sort criteria properties for given report.  
  
To get value of such string in proper form first create template sort settings scheme in report generation GUI. Then export whole template to .xml file and find value for 'SortSchemeData' setting name.



See Also

#### Reference

[ReportBlock Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock.html)
  
[ReportBlock Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock_members.html)