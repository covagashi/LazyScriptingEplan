# LastUsedIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~LastUsedIndex.html

---

Returns number of highest used index. Index value starts from 1. If it is a not indexed-property or if their index is not used, LastUsedIndex is 0.  
An object of MDPropertyValue has to point to online property.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int LastUsedIndex {get;}
```
```

```
```
public:

property int LastUsedIndex {

   int get();

}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [MDNotIndexedPropertyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDNotIndexedPropertyException.html) | Thrown when property is not indexed. |

Example

- [C#](#i-tab-content-ef489791-2312-43f7-87fb-cba50476b147)

```
MDPropertyValue oProperty = m_oTestPart.Properties[ Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_FREE_DATA_VALUE ];

if(oProperty.Definition.IsIndexed)

{

  {

      MDPropertyValue oPropertyElement = oProperty[ i ];

      string sProperty = oPropertyElement.ToString();

  }

}
```
