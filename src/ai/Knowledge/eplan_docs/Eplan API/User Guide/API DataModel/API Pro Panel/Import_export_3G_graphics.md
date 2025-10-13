### Export

Export of 3D graphics is possible to the  STEP  or the  VRML  format:

Export3D::ProjectToStep                          â Exports all installation spaces from a project.

Export3D::InstallationSpacesToStep  â Exports installation spaces.

Export3D::ProjectToVrml                          â Exports all installation spaces from a project.

Export3D::InstallationSpacesToVrml  â Exports installation spaces.

### Import

The item data must be available in the common international  STEP  format (Standard for the Exchange of Product model data).

For each import, a new layout space is generated with the name of the imported  STEP  file.

| C# | Copy Code |
| --- | --- |
| ```  InstallationSpace oInstallationSpace = new Import().Graphics3D(oProject, "c:\\temp\\BK3100\\BK3xxx.stp"); ``` | |

```


```