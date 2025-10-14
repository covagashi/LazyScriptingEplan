# PlaceHolders3DFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolders3DFilter.html

---

This class represents filter of [Eplan.EplApi.DataModel.E3D.PlaceHolder3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D.html)s and derived from it classes.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      **Eplan.EplApi.DataModel.PlaceHolders3DFilter**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class PlaceHolders3DFilter : AbstractDMObjectFilter
```
```

```
```
public ref class PlaceHolders3DFilter : public AbstractDMObjectFilter
```
```

Example

The following example shows how to filter by user-defined properties

- [C#](#i-tab-content-a7c94723-1477-41f0-9404-69e715416e6e)

```

Project myProject = m_oProject; // A valid project
Page myPage = myProject.Pages[0]; // A valid Page object

// Define test property
MultiLangString mlsTestValue = new MultiLangString();
mlsTestValue.AddString(ISOCode.Language.L_de_DE, "Test043c");
string strPropertyIdentyfingName = "Page.Test043c";
UserDefinedPropertyDefinition oUDPD = UserDefinedPropertyDefinition.Create(myProject, strPropertyIdentyfingName, UserDefinedPropertyDefinition.Enums.ClientType.Page);

// Set test property on myPage
myPage.Properties[strPropertyIdentyfingName] = mlsTestValue;

// Search page with property value
DMObjectsFinder objFinder = new DMObjectsFinder(myProject);
PagesFilter pagesFilter = new PagesFilter();
PagePropertyList pagePropertyList = new PagePropertyList();
AnyPropertyId anyPropertyId = new AnyPropertyId(myProject, strPropertyIdentyfingName);

pagePropertyList[anyPropertyId] = mlsTestValue;
pagesFilter.SetFilteredPropertyList(pagePropertyList);
Page[] arrPages1 = objFinder.GetPages(pagesFilter);


```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PlaceHolders3DFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolders3DFilter~_ctor.html) | Default constructor. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolders3DFilter~Name.html) | Name of objects which will be used to filter objects. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor for deterministic finalization of PlaceHolders3DFilter object. (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolders3DFilter~ResetFilter.html) | Overridden. Resets the filter. |

[Top](#top)




See Also

#### Reference

[PlaceHolders3DFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolders3DFilter_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)