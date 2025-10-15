# Constructions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~Constructions.html

---

Gets all constructions that are stored in the parts database.

Syntax

**C#**
**C++/CLI**


public MDConstruction[] Constructions {get;}

public:

property array<MDConstruction^>^ Constructions {

   array<MDConstruction^>^ get();

}


Remarks

The constructions are sorted by it's name
