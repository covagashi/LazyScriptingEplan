# Init(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init(String).html

---

Initializes object with a settings node path.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override void Init( 

   string strScheme

)
```
```

```
```
public:

void Init( 

   String^ strScheme

) override
```
```

#### Parameters

*strScheme*
:   Path to the settings node, for example USER.DXF.SCHEMES

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when scheme with given settings node path can not be found. |

Example

Creating a SchemeSetting object and initializing it with a settings node path

- [C#](#i-tab-content-5346d471-4ef1-4e18-a5f4-e80b97399cbb)

```
SchemeSetting oSchemeSetting = new SchemeSetting();

oSchemeSetting.Init("USER.DXF.SCHEMES");



```
