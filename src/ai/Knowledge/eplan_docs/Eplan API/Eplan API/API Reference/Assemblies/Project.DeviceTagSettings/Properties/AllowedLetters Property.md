# AllowedLetters Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowedLetters.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.AllowedLetters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/All upper-case letters and numbers. It provides possibility to use letters in DeviceTag. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool AllowedLetters {get; set;}
```
```

```
```
public:
property bool AllowedLetters {
   bool get();
   void set (    bool value);
}
```
```

Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.



See Also

#### Reference

[Project.DeviceTagSettings Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings.html)
  
[Project.DeviceTagSettings Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings_members.html)