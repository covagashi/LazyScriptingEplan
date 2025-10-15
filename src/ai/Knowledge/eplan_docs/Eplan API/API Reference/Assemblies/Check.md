# Check

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check.html

---

Class for checking projects or pages.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Check**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class Check
```
```

```
```
public ref class Check
```
```

Example

The following examples shows how to use class Check.

- [C#](#i-tab-content-7354d92c-2005-4c7f-b8c3-18f3835ff411)

```
Check oCheck = new Check();

oCheck.VerifyProject(m_oTestProject);



```

- [C#](#i-tab-content-fcc4b123-1a4c-4d4e-8ee9-b088d9519dbd)

```
Check oCheck = new Check();

oCheck.VerifyPages(new ArrayList(m_oTestProject.Pages));



```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Check Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~_ctor.html) | Default constructor |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~Dispose().html) | Destructor |
| Public Method | [VerifyInstallationSpace](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyInstallationSpace.html) | Overloaded. Starts a check run for the given installation spaces. |
| Public Method | [VerifyMDPartsDatabaseItems](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems.html) | Overloaded. Starts a check run for the given MDPartsDatabaseItems (MDParts). |
| Public Method | [VerifyPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyPages.html) | Overloaded. Starts a check run for the given pages. |
| Public Method | [VerifyProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject.html) | Overloaded. Starts a check run for the given project. |

[Top](#top)
