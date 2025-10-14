# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip~Properties.html

---

.NET Property enabling access to P8 properties of the PlugStrip object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PlugStripPropertyListComplete Properties {get;}
```
```

```
```
public:
new property PlugStripPropertyListComplete^ Properties {
   PlugStripPropertyListComplete^ get();
}
```
```

#### Property Value

P8 properties of the PlugStrip.

Example

- [C#](#i-tab-content-a21988bd-db8c-4047-b718-1a5882e61f61)

```
PlugStrip ps;//a valid PlugStrip
ps.Properties[Properties.PlugStrip.DESIGNATION_PLANT] = "AP";
int cnt = ps.Properties[Properties.PlugStrip.PLUGSTRIP_COUNTOFPE];
```

See Also

#### Reference

[PlugStrip Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)
  
[PlugStrip Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip_members.html)
  
[PlugStripPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStripPropertyList.html)
  
[PlugStrip Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)