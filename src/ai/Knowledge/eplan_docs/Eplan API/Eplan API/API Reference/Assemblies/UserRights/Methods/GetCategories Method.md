# GetCategories Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetCategories.html

---

Returns the identifiers of all existing user rights categories.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public StringCollection GetCategories()
```
```

```
```
public:
StringCollection^ GetCategories();
```
```

#### Return Value

the category identifiers in a string collection. The names are needed in order to add a new right to an existing category.

Example

Example of getting category names that can be displayed in dialogs:

- [C#](#i-tab-content-d0cc526e-161d-444d-b7ca-efbce96304a5)

```

UserRights oUR = new UserRights();
StringCollection oCategoryIDs = oUR.GetCategories();
List<string> lstCategoryNames = new List<string>();
foreach (String strCategoryID in oCategoryIDs)
{
    MultiLangString oMLSCategoryID = new MultiLangString();
    oMLSCategoryID.SetAsString(strCategoryID);
    String strCategoryNameToDisplayInDialog = new Translate().GetStringToDisplayInDialogs(oMLSCategoryID);
    lstCategoryNames.Add(strCategoryNameToDisplayInDialog);
}


```

See Also

#### Reference

[UserRights Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights.html)
  
[UserRights Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights_members.html)