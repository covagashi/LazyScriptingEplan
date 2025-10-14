# InterruptionPointsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter.html

---

This class represents filter of [InterruptionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html) and derived from it classes. The InterruptionPointsFilter can be accessed as a property of a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) object or can be used as a parameter for [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html).

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         [Eplan.EplApi.DataModel.PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html)  
            **Eplan.EplApi.DataModel.InterruptionPointsFilter**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class InterruptionPointsFilter : PlacementsFilter
```
```

```
```
public ref class InterruptionPointsFilter : public PlacementsFilter
```
```

Example

- [C#](#i-tab-content-9bfee94a-296e-48a5-9db1-634ca1cdf574)

```
DMObjectsFinder oFinder = new DMObjectsFinder(m_oTestProject);
InterruptionPointsFilter oIPFilter = new InterruptionPointsFilter();
oIPFilter.Name = "IP";
InterruptionPoint[] oIPTs = oFinder.GetInterruptionPoints(oIPFilter);

```

The following example shows how to filter by user-defined properties

- [C#](#i-tab-content-92648440-2874-4feb-8781-b43cbb565643)

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
| Public Constructor | [InterruptionPointsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~_ctor.html) | Overloaded. |

[Top](#top)



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExactNameMatching](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~ExactNameMatching.html) | Sets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter. Dafault this property is `false`. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~Name.html) | Returns the name that was set to this filter. |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~Page.html) | Overridden. Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [InterruptionPointPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList.html) that [InterruptionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)s matching the filter must have. |

[Top](#top)




See Also

#### Reference

[InterruptionPointsFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)
  
[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[InterruptionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)