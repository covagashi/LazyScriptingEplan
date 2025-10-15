# StartConnectionPointPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~StartConnectionPointPosition.html

---

[Eplan.EplApi.DataModel.ConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html) by which this connection is connected to [Eplan.EplApi.DataModel.Connection.StartSymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~StartSymbolReference.html).

Syntax

**C#**
**C++/CLI**


public ConnectionPointPosition StartConnectionPointPosition {get;}

public:

property ConnectionPointPosition^ StartConnectionPointPosition {

   ConnectionPointPosition^ get();

}


Remarks

This property is `null` if start symbol references has no connection point positions.
