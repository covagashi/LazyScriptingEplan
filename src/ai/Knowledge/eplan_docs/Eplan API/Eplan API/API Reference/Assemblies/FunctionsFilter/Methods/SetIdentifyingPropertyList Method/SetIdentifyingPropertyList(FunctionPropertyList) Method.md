# SetIdentifyingPropertyList(FunctionPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetIdentifyingPropertyList(FunctionPropertyList).html

---

Sets the [FunctionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html) that identifies the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetIdentifyingPropertyList( 
   FunctionPropertyList identPropList
)
```
```

```
```
public:
void SetIdentifyingPropertyList( 
   FunctionPropertyList^ identPropList
)
```
```

#### Parameters

*identPropList*
:   List of the properties which are identifying the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |

Example

The following example shows how to filter by identifying name.

- [C#](#i-tab-content-f2474ebf-9988-4622-a8e1-c5b84d4dcfe1)

```

private Function[] GetSubFunctions(Function oFunction)
{
    FunctionBasePropertyList oIdentNameProps = oFunction.IdentifyingNameParts;
    FunctionPropertyList oFilterOutMainProps = new FunctionPropertyList();
    oFilterOutMainProps.FUNC_MAINFUNCTION = false;
    DMObjectsFinder oFinder = new DMObjectsFinder(m_oProject);
    FunctionsFilter oFilter = new FunctionsFilter();
    oFilter.SetIdentifyingPropertyList(oIdentNameProps);
    oFilter.SetFilteredPropertyList(oFilterOutMainProps);
    Function[] oResult = oFinder.GetFunctions(oFilter);
    return oResult;
}


```

See Also

#### Reference

[FunctionsFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html)
  
[FunctionsFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetIdentifyingPropertyList.html)