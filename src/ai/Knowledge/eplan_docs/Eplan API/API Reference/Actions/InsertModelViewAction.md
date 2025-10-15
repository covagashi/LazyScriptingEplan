# InsertModelViewAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/InsertModelViewAction.html

---

```
Action to insert model view object on a page.
```

  

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME ``` | ``` Project name with full path (optional). If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException"). ``` |
| ``` LAYOUTSPACE ``` | ``` Name of layout space for which model view is created. This parameter is mandatory. ``` |
| ``` STRUCTURE ``` | ``` Structure identifier for which model view is created. This parameter is mandatory if name of layout space is not unique in project. ``` |
| ``` PAGENAME ``` | ``` Full name of page on which model view will be inserted. This parameter is mandatory. ``` |
| ``` X ``` | ``` X-coordinate of model view's lower left corner. This parameter is mandatory. ``` |
| ``` Y ``` | ``` Y-coordinate of model view's lower left corner. This parameter is mandatory. ``` |
| ``` DX ``` | ``` Width of model view. This parameter is mandatory. ``` |
| ``` DY ``` | ``` Height of model view. This parameter is mandatory. ``` |
| ``` VIEWNAME ``` | ``` Name of model view. ``` |
| ``` DESCRIPTION ``` | ``` Description of model view. Value of this parameter can be in multi-language string format. ``` |
| ``` ANGLE ``` | ``` Rotation of the content of model view.  Possible values are:  â¢ 1 - content is rotated 90Â° counter-clockwise;  â¢ 2 - content is rotated 90Â° in opposite direction. ``` |
| ``` SELECTIONSCHEME ``` | ``` Name of the selection scheme. It must be used with cabinet VIEWTYPE parameter. ``` |
| ``` STYLE ``` | ``` Style in which content of model view is displayed. Possible values are: â¢ 0 - Wire frame model; â¢ 1 - Hidden lines; â¢ 2 - Shading; â¢ 3 - Hidden lines / Simplified representation; â¢ 4 - Shading / Simplified representation. ``` |
| ``` ITEMLABELING ``` | ``` Name of the scheme which is applied for labeling the items in the model view. ``` |
| ``` VIEWPOINT ``` | ``` The direction from which objects are seen in model view. Possible values are: â¢ 0 - Default; â¢ 1 - Bottom; â¢ 2 - Top; â¢ 3 - Left; â¢ 4 - Right; â¢ 5 - Front; â¢ 6 - Rear; â¢ 7 - SE isometric; â¢ 8 - SW isometric; â¢ 9 - NE isometric; â¢ 10 - NW isometric; ``` |
| ``` ROOTELEMENTS ``` | ``` Values of property FUNCTION3D_ID_RELATIVE separated by # from 3D placements which will be set as root elements in created model view. ``` |
| ``` SCALESETTING ``` | ``` Type of scaling used to display objects in the model view. Possible values are: â¢ 0 - Automatic; â¢ 1 - Fit; â¢ 2 - Manually defined; ``` |
| ``` SCALE ``` | ``` Scale used to display objects in model view. ``` |
| ``` VIEWTYPE ``` | ``` Type of view used to display objects.  Possible values are: â¢ 0 - Undefined; â¢ 1 - Cabinet; â¢ 2 - EMI; â¢ 3 - Unfolding; â¢ 4 - DrillView; ``` |
| ``` OBJECTID ``` | ``` [OUT] Object id of created model view. ``` |

**Example**

```
Insert model view on a given page:

InsertModelViewAction /PROJECTNAME:C:\Projects\EPLAN\testProject.elk /PAGENAME:"/1" /VIEWNAME:SomeName /LAYOUTSPACE:ProjectLayoutSpaceName
/X:20 /Y:20 /DX:300 /DY:300 /STYLE:1 /VIEWPOINT:5 /SCALESETTING:0 /VIEWTYPE:1
```