# Create(Group,AnyPropertyId) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~Create(Group,AnyPropertyId).html

---

Creates and inserts it into a group ContextPropertyPlacement which displays symbol properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static ContextPropertyPlacement Create( 

   Group group,

   AnyPropertyId propertyId

)
```
```

```
```
public:

static ContextPropertyPlacement^ Create( 

   Group^ group,

   AnyPropertyId^ propertyId

)
```
```

#### Parameters

*group*
:   Group on which object will be inserted.

*propertyId*
:   Property of the object that belongs to the group which will be displayed.

#### Return Value

the newly created ContextPropertyPlacement.

Example

- [C#](#i-tab-content-3ab9c866-73a7-428e-a7d8-0cd5acea21db)

```
MDSymbolVariant variant = symbol.Variants[0];

ContextPropertyPlacement cpp = ContextPropertyPlacement.Create(variant.AsGroup, Properties.Function.FUNC_DEVICETAG_FULLNAME);
```
