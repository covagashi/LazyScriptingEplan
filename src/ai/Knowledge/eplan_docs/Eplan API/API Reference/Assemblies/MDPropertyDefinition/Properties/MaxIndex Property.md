# MaxIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyDefinition~MaxIndex.html

---

Allows to check maximal index value of given property.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual int MaxIndex {get;}
```
```

```
```
public:

virtual property int MaxIndex {

   int get();

}
```
```

#### Property Value

Maximal index of given property.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when MaxIndex property is called on MDPropertyDefinition object with invalid property Id. |

Remarks

Should be called only on MDPropertyDefiniton objects with valid Id.

Example

- [C#](#i-tab-content-95e37682-1a0f-4776-8773-c4ef541c22f8)

```
MDPart oPart = m_MDPartsDatabase.Parts[0]; //a valid part object



//a valid call

int iMaxIndex = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_ADDITIONALTEXT].Definition.MaxIndex;
```
