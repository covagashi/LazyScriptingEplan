The  Component  class represents various Pro Panel items, such as doors, frame profiles, accessories, etc.

Terminal:

| C# | Copy Code |
| --- | --- |
| ```  InstallationSpace oInstallationSpace = new InstallationSpace(); oInstallationSpace.Create(m_oTestProject, "Terminal installation space");  Component oTerminal = new Component(); oTerminal.Create(m_oTestProject, "PXC.3022276", "1"); oTerminal.Parent = oInstallationSpace; ``` | |

![](images/ProPanelAPI/Terminal.jpg)

Plug:

| C# | Copy Code |
| --- | --- |
| ```  InstallationSpace oInstallationSpace = new InstallationSpace(); oInstallationSpace.Create(m_oTestProject, "Plug installation space");  Component oComponent = new Component(); oComponent.Create(m_oTestProject, "Plug.3-pole+PE", "1"); oComponent.Parent = oInstallationSpace; ``` | |

![](images/ProPanelAPI/Plug.jpg)

Power supply:

| C# | Copy Code |
| --- | --- |
| ```  InstallationSpace oInstallationSpace = new InstallationSpace(); oInstallationSpace.Create(m_oTestProject, "Power supply unit installation space"); Component oComponent = new Component(); oComponent.Create(m_oTestProject, @"PXC.2938581", "1"); oComponent.Parent = oInstallationSpace; ``` | |

![](images/ProPanelAPI/PowerSupply.jpg)