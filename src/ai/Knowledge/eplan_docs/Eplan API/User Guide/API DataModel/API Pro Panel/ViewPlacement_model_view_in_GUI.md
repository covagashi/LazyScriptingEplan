Model views are objects used to show a 3D view on a standard EPLAN page.

Example:

| C# | Copy Code |
| --- | --- |
| ```  // Creating 3D objects InstallationSpace oInstallationSpace = new InstallationSpace(); oInstallationSpace.Create(m_oTestProject, "DataModel_081MountingRail_Test001"); Cabinet oCabinet = new Cabinet(); oCabinet.Create(m_oTestProject, "TS 8286.500", "1"); oCabinet.Parent = oInstallationSpace;  // Creating view placement ViewPlacement oViewPlacement = new ViewPlacement(); oViewPlacement.Create(m_oTestProject, m_InstallationSpace); oViewPlacement.Page = oPage; oViewPlacement.Area = new RectangleD(new PointD(0.0, 0.0), new PointD(200.0, 200.0)); oViewPlacement.RootElements = new Placement3D[]{oCabinet}; oViewPlacement.Update(); ``` | |

```

 
```