# IdentifyingNameParts Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~IdentifyingNameParts.html

---

Returns identifying name of the Function.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual FunctionBasePropertyList IdentifyingNameParts {get;}
```
```

```
```
public:
virtual property FunctionBasePropertyList^ IdentifyingNameParts {
   FunctionBasePropertyList^ get();
}
```
```

#### Property Value

Identifying name of the Function by FunctionBasePropertyList.

Example

The following example shows how to filter by identifying name.

- [C#](#i-tab-content-abb8d857-07bd-4aca-8eb7-d113b887e7a0)

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

[FunctionBase Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)
  
[FunctionBase Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase_members.html)