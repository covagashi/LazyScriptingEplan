# GraphicProjectEx(String,String,Format,Int32,Int32,Compression,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1345.html

---

Exports a complete project as image files but instead of pages which [Eplan.EplApi.DataModel.Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) is [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) Returns an array of strings containing names of the created files.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string[] GraphicProjectEx( 

   string strFullLinkFileName,

   string strImagePath,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)
```
```

```
```
public:

array<String^>^ GraphicProjectEx( 

   String^ strFullLinkFileName,

   String^ strImagePath,

   Export.Format imageFormat,

   int iColorDepth,

   int iWidth,

   Export.Compression imageCompression,

   bool bBlackAndWhite

)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project to be exported.

*strImagePath*
:   Directory to which the image files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. A sub\-folder named after the project will be created in which the images will be stored.

*imageFormat*
:   Image format\: Supported export formats are\:

    \* BMP: available color depth: 1, 4, 8, 16, 24 and 32 \* TIF: available color depth: 1, 4, 8, 24 and 32 \* GIF: color depth is irrelevant \* PNG: available color depth: 1, 4, 8, 16, 24 and 32 \* JPG: available color depth: 1, 4, 8, 16, 24 and 32. The enum IMAGE\_FORMAT defines the necessary values. If an invalid format is set, the page will be exported as Tiff.

*iColorDepth*
:   Color depth of the image\: Allowed values are 1, 4, 8, 16, 24, and 32. If an invalid value is set, a color depth of 24 bit us used.

*iWidth*
:   Width of the image in pixels.The height is calculated automatically to keep the aspect ratio of the page.

*imageCompression*
:   Sets the image compression for the Tiff export. This parameter has no influence on other export formats. For the compression according\: CCITT3, CCITT4, and RLE the color depth always is 1, i.e. a binary image is created.

*bBlackAndWhite*
:   If set to true b/w images will be created. This does not influence the image format or the image size.

#### Return Value

An array of strings containing names of the created files.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **UnauthorizedAccessException** | No user rights to create files on the \file system. |
| **ApplicationException** | The internal interface for image export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |

Remarks

The project "strFullLinkFileName" may be open in EPLAN or not. If the project was not already open, it will be opened and after the export it will be closed again.
