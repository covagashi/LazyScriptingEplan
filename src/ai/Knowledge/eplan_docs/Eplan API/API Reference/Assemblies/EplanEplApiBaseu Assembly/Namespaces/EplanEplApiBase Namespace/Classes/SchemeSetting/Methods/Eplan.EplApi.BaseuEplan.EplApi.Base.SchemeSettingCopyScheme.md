Copy an existing scheme.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public void CopyScheme( 
   string strSettingsSourceNodeName,
   string strSettingsTargetNodeName,
   MultiLangString mlTargetNewName,
   MultiLangString mlTargetDescription
)
```
```

```
```
public:
void CopyScheme( 
   String^ strSettingsSourceNodeName,
   String^ strSettingsTargetNodeName,
   MultiLangString^ mlTargetNewName,
   MultiLangString^ mlTargetDescription
)
```
```

#### Parameters

*strSettingsSourceNodeName*
:   Node name of the source scheme

*strSettingsTargetNodeName*
:   Node name of the new scheme

*mlTargetNewName*
:   Displayed name of the new scheme

*mlTargetDescription*
:   Description of the new scheme

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme. The scheme with this strSettingsTargetNodeName already exists or the source scheme does not exist. |



See Also

#### Reference

[SchemeSetting Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)
  
[SchemeSetting Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html)