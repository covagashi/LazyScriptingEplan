# ExactNameMatching Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~ExactNameMatching.html

---

Gets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ExactNameMatching {get; set;}
```
```

```
```
public:

property bool ExactNameMatching {

   bool get();

   void set (    bool value);

}
```
```

Example

- [C#](#i-tab-content-75e962fe-f2ad-48b8-ba43-2392ce2f0ec0)

```
Project proj;//a valid project



proj.Filter.ExactNameMatching = true;

proj.Filter.Name = "=AP+ST1/1";

Page[] pages = proj.Pages; //now we have all pages named exactly "=AP+ST1/1"
```

- [C#](#i-tab-content-37d67a07-8eb8-4a49-93df-4df44a8bf2ed)

```
Project proj;//a valid project



p.Filter.ExactNameMatching = false;

proj.Filter.Name = "=AP+ST1";

pages = p.Pages; //now we have all pages with names starting with "=AP+ST1"
```
