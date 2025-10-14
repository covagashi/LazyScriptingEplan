# ReportBlock Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~ReportBlock.html

---

`ReportBlock` which contains data describing report from this page.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public ReportBlock ReportBlock {get;}
```
```

```
```
public:
property ReportBlock^ ReportBlock {
   ReportBlock^ get();
}
```
```

Remarks

If a report is assign to a page then this property returns an object which contains data describing it. If no report is assign then this property returns `null`.



See Also

#### Reference

[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)
  
[Page Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page_members.html)
  
[ReportBlock Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock.html)