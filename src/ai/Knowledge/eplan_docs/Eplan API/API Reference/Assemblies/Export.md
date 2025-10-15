# Export

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export.html

---

Class for exporting projects and project data to various formats. The following example shows how to use class Export.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Export**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class Export
```
```

```
```
public ref class Export
```
```

Example

The following example shows how to use class Export.

- [C#](#i-tab-content-02c9f066-eb04-477e-9ec2-7548e20944a0)

```
Export oExport = new Export();

ArrayList oPagesAL = new ArrayList();

oPagesAL.Add(m_oProject.Pages[2]);

oPagesAL.Add(m_oProject.Pages[3]);

oExport.PdfPages(oPagesAL, "EPLAN_default_value", "$(TMP)\\1.pdf", Export.DegreeOfColor.BlackAndWhite, true, "", true);



```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Export Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~_ctor.html) | Overloaded. |

[Top](#top)




Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~Dispose().html) | Destructor |
| Public Method | [DxfDwgPage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgPage.html) | Overloaded. Exports a page of a project as a DXF/DWG file. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [DxfDwgPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgPages.html) | Overloaded. Exports pages of a project as a DXF/DWG file. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [DxfDwgPagesToDisk](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgPagesToDisk.html) | Exports pages of a project as a DXF/DWG file. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [DxfDwgPageToDisk](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgPageToDisk.html) | Overloaded. Exports a page of a project as a DXF/DWG file. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [DxfDwgProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgProject.html) | Overloaded. Exports a complete project as DXF/DWG files. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [DxfDwgProjectToDisk](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~DxfDwgProjectToDisk.html) | Overloaded. Exports a complete project as DXF/DWG files. Export settings are taken from the scheme passed in the 'sScheme' parameter |
| Public Method | [GraphicPage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicPage.html) | Overloaded. Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) |
| Public Method | [GraphicPageEx](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicPageEx.html) | Overloaded. Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) Returns the name of the created file. |
| Public Method | [GraphicPageEx2](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicPageEx2.html) | Exports a page of a project as image file. [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) of page can not be [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) |
| Public Method | [GraphicProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicProject.html) | Overloaded. Exports a complete project as image files but instead of pages which [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) is [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) |
| Public Method | [GraphicProjectEx](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~GraphicProjectEx.html) | Overloaded. Exports a complete project as image files but instead of pages which [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) is [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) Returns an array of strings containing names of the created files. |
| Public Method | [PdfPages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~PdfPages.html) | Overloaded. Exports pages of one project as PDF file. |
| Public Method | [PdfProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~PdfProject.html) | Overloaded. Exports one project as PDF file. |
| Public Method | [PXFProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export~PXFProject.html) | Overloaded. Exports a project in PXF format. |

[Top](#top)
