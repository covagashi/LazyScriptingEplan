You can influence the parts import process from the Eplan Data Portal by changing the behaviour just before the import to P8 and just after the import to P8. The  EDataPreImportAction  must be implemented in order to display or modify the parts before the import and the implementation of  EDataPostImportAction  is necessary for influencing the parts after the import.

The following example uses a custom add-in to show the part path in a message box before importing from the Data Portal using the  EDataPreImportAction:

* [C#](#i-tab-content-9beb5ea7-9b38-4f19-b12e-1e533a30f9c0)

```

public class EDataPreImportAction : IEplAction
{
    public bool OnRegister(ref string Name, ref int Ordinal)
    {
        Ordinal = 20;
        Name = "EDataPreImportAction";
        return true;
    }

    public bool Execute(ActionCallingContext oActionCallingContext)
    {
        string filename = null;
        oActionCallingContext.GetParameter("filenames", ref filename);
        MessageBox.Show($"This is the path to the imported part: {filename}");
        return true;
    }

}
```

In the same way, the part can be queried or edited after the import via the  EDataPostImportAction.