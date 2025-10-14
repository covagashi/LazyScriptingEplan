# Indexes Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Indexes.html

---

Returns the valid / actually used indexes. It can be used with the PropertyValue::operator []. To use the Indexes property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property).

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

- [C#](#i-tab-content-29609f00-d299-4163-a890-24502af90438)

```

Function function = page.Functions[0]; // A valid Function object

// Get all used indexes for indexed property FUNC_CONNECTIONDESIGNATION
int[] indexes = function.Properties.FUNC_CONNECTIONDESIGNATION.Indexes;

// Iterate over all indexes of FUNC_CONNECTIONDESIGNATION property
PropertyValue propertyValue = function.Properties.FUNC_CONNECTIONDESIGNATION;

if(propertyValue.Definition.IsIndexed)
{
    foreach (int index in propertyValue.Indexes)
    {
        PropertyValue propertyElement = propertyValue[index];
        string sProperty = propertyElement.ToString();
    }
}


```

See Also

#### Reference

[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[PropertyValue Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue_members.html)
  
[MaxIndex Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~MaxIndex.html)
  
[IsIndexed Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsIndexed.html)
  
[LastUsedIndex Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~LastUsedIndex.html)