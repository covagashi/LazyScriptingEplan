To create a page in a project, the  Eplan.EplApi.DataModel.Page  class provides a  Create  method. You first instantiate an empty  Page  object and then call  Create. The method takes three parameters: first the project, in which the page is to be created, then the type of the page, and finally a  PagePropertyList  with the identifying properties of the page.

The types of pages you can create are listed in the  DocumentTypeManager.DocumentType  enumeration.

The following example shows how to create a schematic page:

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

// Create new schematic page in current project
PagePropertyList oPagePropList = new PagePropertyList();
// Set Plant
oPagePropList[Properties.Page.DESIGNATION_PLANT] = "P1";
// Set Location
oPagePropList[Properties.Page.DESIGNATION_LOCATION] = "L1";
Page oNewPage = new Page();
oNewPage.Create(m_oTestProject, DocumentTypeManager.DocumentType.Circuit, oPagePropList);
```

```

' Create new schematic page in current project
Dim oPagePropList As New PagePropertyList()
' Set Plant
oPagePropList(Properties.Page.DESIGNATION_PLANT) = PropertyValue.op_Implicit("P1")
' Set Location
oPagePropList(Properties.Page.DESIGNATION_LOCATION) = PropertyValue.op_Implicit("L1")
' Set Counter
oPagePropList(Properties.Page.PAGE_COUNTER) = PropertyValue.op_Implicit(4)
Dim oNewPage As New Page()
oNewPage.Create(m_oTestProject, DocumentTypeManager.DocumentType.Circuit, oPagePropList)
```

Remarks

Please mind that when you create a page, you cannot set descriptive properties in the  PropertyList  mentioned above. Only parts of the page name can be set using this list.

Other properties need to be set after creating the page by  Page.Properties.