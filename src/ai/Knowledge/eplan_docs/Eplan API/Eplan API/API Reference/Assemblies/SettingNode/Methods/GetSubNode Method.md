# GetSubNode Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetSubNode.html

---

Determines a child node.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual SettingNode GetSubNode( 
   string strSubNodePath
)
```
```

```
```
public:
virtual SettingNode^ GetSubNode( 
   String^ strSubNodePath
)
```
```

#### Parameters

*strSubNodePath*
:   Indicates the path of the child node (relative to path of the node, path starts after the path of the node).

#### Return Value

The child node.If child node doesn't exist,NULL value is returned.

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |



See Also

#### Reference

[SettingNode Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html)
  
[SettingNode Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode_members.html)