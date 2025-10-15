# Create(Page,String,PointD,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~Create(Page,String,PointD,PointD).html

---

Creates the Image object.

Syntax

**C#**
**C++/CLI**


public void Create( 

   Page page,

   string fileName,

   PointD pntStart,

   PointD pntEnd

)

public:

void Create( 

   Page^ page,

   String^ fileName,

   PointD pntStart,

   PointD pntEnd

)


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the Image will be placed on.

*fileName*
:   path to graphical file containing the image

*pntStart*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) representing 1st image's corner

*pntEnd*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) representing 2nd image's corner

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Image cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Image has already been created. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
