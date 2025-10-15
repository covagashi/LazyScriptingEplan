# Pages Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Pages.html

---

Returns pages, which are contained in the macro.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override Page[] Pages {get;}
```
```

```
```
public:

property array<Page^>^ Pages {

   array<Page^>^ get() override;

}
```
```

#### Property Value

Array of pages. Array's property `Length` gives information about amount of found Pages in the macro.
