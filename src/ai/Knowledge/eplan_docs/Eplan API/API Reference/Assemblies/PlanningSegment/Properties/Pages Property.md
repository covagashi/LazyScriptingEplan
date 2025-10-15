# Pages Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Pages.html

---

Returns collection of all pages assigned to the planning segment.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Page[] Pages {get;}
```
```

```
```
public:

property array<Page^>^ Pages {

   array<Page^>^ get();

}
```
```

Example

Example shows how to assign pages to planning segment.

- [C#](#i-tab-content-4213d4fd-cae2-41d7-8337-8997344558e3)

```
//for newly created PCT loop there is no pages assigned

Page[] arrPages = oPCTLoop.Pages;

//oPCTLoop.Pages.Length == 0



//assign pages

oPage1.PlanningSegment = oPCTLoop;

oPage2.PlanningSegment = oPCTLoop;



//pages are assigned

//oPCTLoop.Pages.Length == 2



//remove assignment from one page

oPage1.PlanningSegment = null;



//oPCTLoop.Pages.Length == 1



```
