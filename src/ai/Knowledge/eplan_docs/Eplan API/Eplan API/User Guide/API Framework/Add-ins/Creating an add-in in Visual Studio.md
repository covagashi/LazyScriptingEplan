# Creating an add-in in Visual Studio

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/AddinInVisualStudio.html

---

Compared to using a text editor and the compiler provided by the .NET Framework, it is much easier to create an add-in with using a development environment such as Visual Studio 2022.

Eplan templates are installed in Visual Studio with the API setup, which can be downloaded from the [Eplan homepage](https://www.eplan.de/services/downloads/eplan-api/).   
To create an add-in, just create a project in Visual Studio using the "Eplan Api Addin" template from C# Projects:

![](images/New_Project.jpg)

 The new project already references the essential Eplan API assemblies and a file with the module class:

![](images/New_Project2.jpg)

You can add a new Action class by the Add New Item menu point and selecting the template "Eplan Action":

![](images/New_Action.jpg)

For Visual Basic, the work flow is identical.