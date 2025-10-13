The following example shows how to open the default parts database:

* [C#](#i-tab-content-f61f5169-d738-4dd6-a177-da8cc2e02a34)

```

MDPartsManagement oPartsManagement = new MDPartsManagement();
MDPartsDatabase partsDatabase = oPartsManagement.OpenDatabase();
```

It is also possible to open a selected parts database from a file:

* [C#](#i-tab-content-f9c56d80-135d-4161-b539-4ffea77765f7)

```

MDPartsDatabase partsDatabase = new MDPartsManagement().OpenDatabase("C:\\PathToDirectory\\DataBase.alk");
```

Then you can check information about the open database:

* [C#](#i-tab-content-d4e41da8-ce6b-4b1d-aa75-a6f2bd1c2f75)

```

// Show database name
var bdName = MDPartsManagement.SelectedPartsDatabaseAsString;
new Decider().Decide(EnumDecisionType.eOkDecision, bdName, "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Check if database is open
if (partsDatabase.IsOpen);
    new Decider().Decide(EnumDecisionType.eOkDecision, "DataBase is open", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Check if database is readonly
if (!partsDatabase.IsReadOnly) ;
    new Decider().Decide(EnumDecisionType.eOkDecision, "DataBase is not readolny", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Get database version
var dataBaseVersion = partsDatabase.Version;

// Get database type
var dataBaseType = partsDatabase.Type;

// Check if database scheme is up to date
if (partsDatabase.IsSchemeUpToDate) ;
  new Decider().Decide(EnumDecisionType.eOkDecision, "Scheme is up to date", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
```

Finally, close the database:

* [C#](#i-tab-content-b6eeb556-34e4-4991-955e-92e56bdb7107)

```

partsDatabase.Close();
```