The  Connection3D  class represents a 3D connection between two  Placement3D  objects.

It inherits from the "normal" Connection.

| C# | Copy Code |
| --- | --- |
| ```           // Creating a 3D connection that exists between two 3D functions Connection3D oConnection3DNoConnectionPoints = new Connection3D(); oConnection3DNoConnectionPoints.Create(oFunction3D_1, oFunction3D_2);  // Creating a 3D connection using connection point indexes Connection3D oConnection3D = new Connection3D(); oConnection3D.Create(oComponent3D_1, 1, oComponent3D_2, 2);  // Route connections List<StorableObject> olist = new List<StorableObject>(); olist.Add(oPlacement3D_1); olist.Add(oPlacement3D_2); ConnectionService3D oConnectionService3D = new ConnectionService3D(); oConnectionService3D.RouteConnections(olist); ``` | |

![](images/ProPanelAPI/Connection3D.jpg)