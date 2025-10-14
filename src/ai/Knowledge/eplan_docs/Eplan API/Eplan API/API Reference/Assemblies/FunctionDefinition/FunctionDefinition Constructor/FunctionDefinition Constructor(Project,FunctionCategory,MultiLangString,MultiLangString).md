# FunctionDefinition Constructor(Project,FunctionCategory,MultiLangString,MultiLangString)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic210.html

---

Constructs and initializes a FunctionDefinition object with the specified function's category, group and ID. Note: The specified function definition must exist in the project's standard function definitions library

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public FunctionDefinition( 
   Project prj,
   FunctionCategory funcCategory,
   MultiLangString funcGroupName,
   MultiLangString funcDefName
)
```
```

```
```
public:
FunctionDefinition( 
   Project^ prj,
   FunctionCategory funcCategory,
   MultiLangString^ funcGroupName,
   MultiLangString^ funcDefName
)
```
```

#### Parameters

*prj*


*funcCategory*
:   Category of the function definition.

*funcGroupName*
:   Group of the function definition (e.g. "Ader/Draht").

*funcDefName*
:   Identification name of the function definition (e.g. "BrÃ¼cke"). This name for a specific function definition is returned by the FunctionDefinition::Name property.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the specified function definition (category, group and ID) doesn't exists in the project's function definitions library. |

Remarks

Note: Only the first language strings passed by funcGroupName and funcIDName are taken into account.

Example

- [C#](#i-tab-content-ab7a805f-e06d-42f2-b6fb-a84d3e1d41e2)

```
MultiLangString grpName = new MultiLangString();
grpName.AddString(ISOCode.Language.L_de_DE, "Ader/Draht");
MultiLangString idName = new MultiLangString();
idName.AddString(ISOCode.Language.L_de_DE, "Brücke");

FunctionDefinition fctDef = new FunctionDefinition(prj, funcCategory, grpName, idName);
```

See Also

#### Reference

[FunctionDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html)
  
[FunctionDefinition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~_ctor.html)