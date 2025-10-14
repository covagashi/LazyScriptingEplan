### Mounting panel (with article):

 ``` 
 MountingPanel oMountingPanel = new MountingPanel();
 oMountingPanel.Create(m_oTestProject, "MP AE 1031.500", "1");
 oMountingPanel.Parent = oCabinet; // Can also be, for example, InstallationSpace
 ``` 



### Free mounting panel:


 ``` 
 MountingPanel oMountingPanel = new MountingPanel();
 oMountingPanel.Create(m_oTestProject, 300.0, 400.0, 2.0);
 oMountingPanel.Parent = oCabinet;
 ``` 

