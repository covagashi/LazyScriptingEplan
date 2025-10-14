Every project has its own set of settings. To get and set these settings, as well as to create new settings, the  DataModel  namespace provides a class called  ProjectSettings. It has similar methods as the settings class in  Eplan.EplApi.Base, but an instance of this class is initialized with the project object. Unlike the "normal" settings, the project settings keys **don't** start with "PROJECT", where the other settings start with "USER", "STATION", or "COMPANY".

Example for project related settings Projects > <project name> > Connections > General:

| Example Title | Copy Code |
| --- | --- |
| ``` 
 <?xml version="1.0" encoding="utf-8" ?>
 <Settings ver="2.4.1" format="2">
  <CAT name="PROJECT">
   <MOD name="EsConnection">
    <Setting name="ManageConnectionsInNDPDialog" type="bool">
     <Val>0</Val>
    </Setting>
    <Setting name="ManageSaddleJumperConnPointsInNDPDialog" type="bool">
     <Val>0</Val>
    </Setting>
    <Setting name="SortConnectionsByPlacement" type="bool" desc="2058">
     <Val>0</Val>
    </Setting>
   </MOD>
  </CAT>
 </Settings>
 ``` | |

The following example shows how to get the project setting for the project display languages.

* [C#](#i-tab-content-CS)
* [VB](#i-tab-content-VB)

```

Eplan.EplApi.DataModel.ProjectSettings projectSettings =
          new Eplan.EplApi.DataModel.ProjectSettings(oProject);
string languages = projectSettings.GetExpandedStringSetting("TRANSLATEGUI.DISPLAYED_LANGUAGES", 0)
```

```

Dim projectSettings As New Eplan.EplApi.DataModel.ProjectSettings(oProject)
Dim languages As String
languages = projectSettings.GetExpandedStringSetting("TRANSLATEGUI.DISPLAYED_LANGUAGES", _
                                                       System.Convert.ToUInt32(0))
```
