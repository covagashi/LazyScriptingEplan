The  InstallationSpace  represents a 3-dimensional space where objects can be located.

It is also a root node for other 3D objects in the Layout spaces navigator.

The following example shows how to create an  InstallationSpace:

 ``` 
 InstallationSpace oInstallationSpace = new InstallationSpace();
 oInstallationSpace.Create(oProject, "InstallationSpace test");
 ``` 



We can retrieve existing  InstallationSpaces  from a project this way:

 ``` 
 InstallationSpace[] arrInstallationSpace = oProject.InstallationSpaces;
 ``` 

In the GUI it is called Layout space. It is independent of pages in a project.

