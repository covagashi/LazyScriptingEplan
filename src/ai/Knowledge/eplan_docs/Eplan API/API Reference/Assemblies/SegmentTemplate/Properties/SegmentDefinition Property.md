# SegmentDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate~SegmentDefinition.html

---

Definition object of this templates.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual SegmentDefinition SegmentDefinition {get; set;}
```
```

```
```
public:

virtual property SegmentDefinition^ SegmentDefinition {

   SegmentDefinition^ get();

   void set (    SegmentDefinition^ value);

}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when new definition has different type then current definition. |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |
| [System.InvalidOperationException](#) | Thrown when template is already assigned to planning object. |
