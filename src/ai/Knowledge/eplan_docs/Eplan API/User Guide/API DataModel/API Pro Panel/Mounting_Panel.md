### Mounting panel (with article):

| C# | Copy Code |
| --- | --- |
| ```  MountingPanel oMountingPanel = new MountingPanel(); oMountingPanel.Create(m_oTestProject, "MP AE 1031.500", "1"); oMountingPanel.Parent = oCabinet; // Can also be, for example, InstallationSpace ``` | |

![](images/ProPanelAPI/MountingPanel.jpg)

### Free mounting panel:

| C# | Copy Code |
| --- | --- |
| ```  MountingPanel oMountingPanel = new MountingPanel(); oMountingPanel.Create(m_oTestProject, 300.0, 400.0, 2.0); oMountingPanel.Parent = oCabinet; ``` | |

![](images/ProPanelAPI/FreeMountingPanel.jpg)