# Write Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~Write.html

---

Writes all settings to a file.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Write( 

   string strFileName

)
```
```

```
```
public:

void Write( 

   String^ strFileName

)
```
```

#### Parameters

*strFileName*
:   Indicates the full file name of the settings file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strFileName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strFileName` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |

Example

Example how to export main settings node by SettingNode:

- [C#](#i-tab-content-5d638278-e73b-48d9-95ea-3a5892f1677e)

```
SettingNode oSettingNode = new SettingNode("USER");

oSettingNode.Write("G:\\temp\\1.xml");
```
