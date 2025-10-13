The  Plane  class represents a surface object on which components can be placed.

| C# | Copy Code |
| --- | --- |
| ```  MountingPanel oMountingPanel = new MountingPanel(); oMountingPanel.Create(oTestProject, "MP AE 1030.500", "1"); oMountingPanel.Parent = m_oInstallationSpace; Plane oPlane1 = oMountingPanel.Children[0] as Plane; Plane oPlane2 = oMountingPanel.Children[1] as Plane; ``` | |

![](images/ProPanelAPI/Plane.jpg)