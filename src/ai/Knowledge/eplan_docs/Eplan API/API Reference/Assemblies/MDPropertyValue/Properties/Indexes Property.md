# Indexes Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Indexes.html

---

Returns array of indexes for which property value is not empty. It can be used with MDPropertyValue::operator [];

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int[] Indexes {get;}
```
```

```
```
public:

property array<int>^ Indexes {

   array<int>^ get();

}
```
```

Example

- [C#](#i-tab-content-a4371bf3-8173-4b1b-ab11-fbe51ed9ad90)

```
MDPart oPart = m_MDPartsDatabase.Parts[0];//a valid part object

MDPropertyValue oProperty = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_FREE_DATA_VALUE;];

if (oProperty.Definition.IsIndexed)

{

	foreach (int index in oProperty.Indexes)

	{

		MDPropertyValue oPropertyElement = oProperty[index];

		string sProperty = oPropertyElement.ToString();

	}

}
```
