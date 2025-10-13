Initializes object with a settings node path.

Syntax

* [C#](#i-syntax-CS)
* [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void Init( 
   string strScheme
)
```
```

```
```
public:
virtual void Init( 
   String^ strScheme
)
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

* [C#](#i-tab-content-9027f146-f740-4eb1-a9e7-04e584bcd136)

```
SchemeSetting oSchemeSetting = new SchemeSetting();
oSchemeSetting.Init("USER.DXF.SCHEMES");

```

See Also

#### Reference

[SchemeSetting Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html)
  
[SchemeSetting Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html)