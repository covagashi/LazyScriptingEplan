# Property(MDSymbol) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~Property(MDSymbol).html

---

Method used by operator[] in order to access properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue Property( 

   Properties.MDSymbol id

) {get; set;}
```
```

```
```
public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(Properties.MDSymbol id);

   void set (Properties.MDSymbol id, MDPropertyValue^ value);

}
```
```

#### Parameters

*id*
:   Identifier of the MDSymbol's property

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
| [MDPropertyReadOnlyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyReadOnlyException.html) | MDPropertyReadOnlyException |
| [MDSettingValueFailedException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSettingValueFailedException.html) | MDSettingValueFailedException |
