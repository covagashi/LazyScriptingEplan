# TemplatesFromArticles Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~TemplatesFromArticles.html

---

Returns set of templates from articles assigned to this object or to its segment template.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public StorableObject[] TemplatesFromArticles {get;}
```
```

```
```
public:

property array<StorableObject^>^ TemplatesFromArticles {

   array<StorableObject^>^ get();

}
```
```

Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned then set of templates from articles of the segment template is returned. If `not` then set of templates from articles of this object is returned.
