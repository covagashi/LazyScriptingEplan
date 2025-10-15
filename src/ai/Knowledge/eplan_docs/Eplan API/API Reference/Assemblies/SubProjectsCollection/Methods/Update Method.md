# Update Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProjectsCollection~Update.html

---

Updates project from subproject.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Update( 

   SubProject pSubProject

)
```
```

```
```
public:

void Update( 

   SubProject^ pSubProject

)
```
```

#### Parameters

*pSubProject*

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if subproject is in incorrect state and update is not possible. |
| [System.ArgumentNullException](#) | Thrown when parameter is null. |

Example

Example of updating a master project with content of subproject

- [C#](#i-tab-content-940b1019-a062-4641-9e60-15d81e4e4650)

```


//Update from second subproject

oSubProjectsCollection.Update(oSubProjectsCollection[0]);





```
