## Manual unregistration of an add-on

After clicking the Add-ons option (as shown in figure 1), the same dialog â as shown in figure 2 â will appear. After deactivating the add-on,  the button ![](images/Addons_files/image012.png) will be enabled.

![](images/Addons_files/image013.jpg)

*Figure 7: Unregister add-ons*

By clicking on the delete button, the add-on will be deleted from the list and also will the belonging add-in be deleted from the list of the API module dialog.

![](images/Addons_files/image014.gif)Warning:

The delete button ![](images/Addons_files/image012.png) will only be enabled, when the add-on was manually registered before.

### Unregistration of an add-on via an action

It is also possible to unregister an add-on via an action call.

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| Path | The path where the add-on is located |
| InstallFile | The complete path to the  install.xml |

![](images/Addons_files/image007.gif)Example:

Registering Add-ons:

XSettingsUnregisterAction /Path:c:\MyAddOn

XSettingsUnregisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml

After you unregistered the add-on via the action call, you may want to verify if the add-on is actually unregistered in the Add-ons dialog and the belonging add-in files are unloaded.

## Automatic unregistration of an add-on

Like there are two ways to initiate the automatic registration of an add-on when Eplan is started, there are two ways to reset this setting as well.

### Automatic unregistration with registry settings

To reset the automatic registration with the Registry Editor, you only have to change the value data to "FALSE" (see figure 4).

### Automatic unregistration with company settings

To reset the automatic registration with company settings, you should leave the File path for automatic add-on registration field in the Settings: Add-ons dialog â as shown in figure 6 â **empty**.