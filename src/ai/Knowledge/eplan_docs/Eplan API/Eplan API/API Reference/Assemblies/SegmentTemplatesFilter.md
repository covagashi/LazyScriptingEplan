# SegmentTemplatesFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter.html

---

This class represents filter for [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)s objects.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         **Eplan.EplApi.DataModel.SegmentTemplatesFilter**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class SegmentTemplatesFilter : StorableObjectsFilter
```
```

```
```
public ref class SegmentTemplatesFilter : public StorableObjectsFilter
```
```

Example

- [C#](#i-tab-content-83c880fd-6166-44be-9efa-8608c987c922)

```
DMObjectsFinder oFinder = new DMObjectsFinder(m_oTestProject);
StorableObjectsFilter oFilter = new StorableObjectsFilter();
oFilter.Page = m_oTestProject.Pages[10];
StorableObject[] oSO = oFinder.GetStorableObjects(oFilter);

```

The following example shows how to filter by user-defined properties

- [C#](#i-tab-content-6a0c697c-f786-4f77-8d01-365e39af57c6)

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
| Public Constructor | [SegmentTemplatesFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~Page.html) | Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. (Inherited from [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList.html) that [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html)s matching the filter must have. |

[Top](#top)




See Also

#### Reference

[SegmentTemplatesFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[SegmentDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)