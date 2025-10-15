# AddModule() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~AddModule().html

---

Adds new module to article.

Syntax

**C#**
**C++/CLI**


public Article.Module AddModule()

public:

Article.Module^ AddModule();


#### Return Value

Object representing new module of article.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when type of article is incorrect. |

Remarks

Newly created module is added to [ArticleModules](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleModules.html) as last one. Modification of modules collection assigned to article is done only in project database. Changes are `not` visible in system parts database until synchronization of parts is done.

It is not allowed to add modules to article which are not of type: `Module`. To check if part has correct type see property ARTICLE\_PARTTYPE.
