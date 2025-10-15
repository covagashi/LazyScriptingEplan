# ReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDUserDefinedPropertyDefinition~ReadOnly.html

---

Check if a given property is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override bool ReadOnly {get;}
```
```

```
```
public:

property bool ReadOnly {

   bool get() override;

}
```
```

#### Property Value

true : Property is read-only

false : Property is not read-only

Remarks

Should be called only on MDPropertyDefiniton objects with valid Id.

Example

- [C#](#i-tab-content-f4c40db4-dd8b-4401-b5f5-a74866700dfd)

```
MDPart oPart = m_MDPartsDatabase.Parts[0];//a valid part object



//a valid call

bool bReadOnly = oPart.Properties.ARTICLE_HEIGHT.Definition.ReadOnly;
```
