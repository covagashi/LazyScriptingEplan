# NameParts Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~NameParts.html

---

Gets/Sets the name of a page.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PagePropertyList NameParts {get; set;}
```
```

```
```
public:

property PagePropertyList^ NameParts {

   PagePropertyList^ get();

   void set (    PagePropertyList^ value);

}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Cannot set name of the page |

Remarks

Note: When using this property to set a page's name, it is not validated whether the value being set is correct and not yet existing in the project. Also if PAGE\_COUNTER property is not specified, it is NOT set to a default value automatically. (Unlike when using [SetName(PagePropertyList)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetName(PagePropertyList).html) method.) Changing identifying page properties, such as the higher-level function, DOES NOT rename all the DTs for the same higher-level function on the page as it is done when setting a page name in GUI. The property list being set may contain the following properties: Â· DESIGNATION\_PLANT Â· DESIGNATION\_SUBPLANT1 Â· DESIGNATION\_SUBPLANT2 Â· DESIGNATION\_SUBPLANT3 Â· DESIGNATION\_LOCATION Â· DESIGNATION\_SUBLOCATION1 Â· DESIGNATION\_SUBLOCATION2 Â· DESIGNATION\_SUBLOCATION3 Â· DESIGNATION\_SUBLOCATION4 Â· DESIGNATION\_SUBLOCATION5 Â· PAGE\_COUNTER Â· PAGE\_SUBCOUNTERER To check whether a property is a name property, please use PropertyDefinition::IsNamePart. For more information about page name syntax please see chapter 'Dialog Settings: DT syntax check' in Eplan documentation.

Example

- [c#](#i-tab-content-f9ca1542-061c-4a8a-a9ed-f4f3e20833f2)

```
Page pg;

PagePropertyList pagePropList = new PagePropertyList();

pagePropList.DESIGNATION_PLANT = "API_Test";

pagePropList.DESIGNATION_LOCATION = "New_Schematic";

pagePropList.PAGE_COUNTER = 002;

pg.NameParts = pagePropList;
```
